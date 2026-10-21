#!/usr/bin/env python3
"""Check internal links and anchors in docs-content MDX files.

Mirrors how the docs website resolves content:
- /<slug>/ -> pages/<slug>/index.mdx, else pages/<slug>.mdx
- /tutorials/<slug>/ -> tutorials/<slug>/index.mdx
- heading ids use github-slugger, deduplicated per file; headings of
  imported macros (@macros/...) are slugged separately and count as anchors
  of the importing page.

Usage (from the docs-content root):
    python3 bin/check-internal-links.py                 # scan pages/, tutorials/, macros/, blocks/, docs/, changelog/
    python3 bin/check-internal-links.py pages/instances # scan a subset
    python3 bin/check-internal-links.py --no-anchors    # skip #anchor checks
    python3 bin/check-internal-links.py --trailing-slash # also flag /page links without a trailing slash

Exits with status 1 when broken links are found.
"""
import argparse
import os
import re
import sys
import unicodedata
from functools import lru_cache
from urllib.parse import unquote, urlsplit

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PUBLIC_DIR = os.path.join(ROOT, "..", "public")
SCAN_DIRS = ("pages", "tutorials", "macros", "changelog")
# Style guide and templates show example links, broken on purpose
SKIP_FILES = {"pages/guidelines.mdx"}
SKIP_FILE_RE = re.compile(r"(TEMPLATE.*\.mdx$|^docs/templates/)")
DOCS_URL_PREFIXES = ("https://www.scaleway.com/en/docs", "http://www.scaleway.com/en/docs")
# Routes served by the website app rather than by an MDX file
APP_ROUTES = {"", "changelog", "faq", "troubleshooting", "tutorials", "ai-search"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$")
MD_LINK_RE = re.compile(r"\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
REF_LINK_RE = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*(\S+)")
HREF_RE = re.compile(r"""\b(?:href|to)\s*=\s*["']([^"']+)["']""")
BARE_DOCS_URL_RE = re.compile(r"https?://www\.scaleway\.com/en/docs[^\s)\"'<>`]*")
HTML_ANCHOR_RE = re.compile(r"""<[a-zA-Z][^>]*\b(?:id|name)\s*=\s*["']([^"']+)["']""")
MACRO_IMPORT_RE = re.compile(r"""^import\s+\w+\s+from\s+["'](@macros/[^"']+)["']""", re.M)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.S)


def github_slug(text):
    """Port of github-slugger's slug(): lowercase, drop punctuation, spaces to hyphens."""
    out = []
    for char in text.lower():
        if char in " -_" or unicodedata.category(char)[0] in "LNM":
            out.append(char)
    return "".join(out).replace(" ", "-")


def heading_text(raw):
    """Approximate hast toText() of a markdown heading."""
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", raw)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"(\*\*|__|\*|_)(\S(?:.*?\S)?)\1", r"\2", text)
    return text.strip()


def strip_frontmatter(content):
    match = FRONTMATTER_RE.match(content)
    if not match:
        return content, 0
    return content[match.end():], match.group(0).count("\n")


def content_lines(content):
    """Yield (line number, line) outside fenced code blocks, frontmatter removed."""
    body, offset = strip_frontmatter(content)
    in_fence = False
    for index, line in enumerate(body.split("\n"), start=offset + 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield index, line


@lru_cache(maxsize=None)
def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


@lru_cache(maxsize=None)
def own_anchors(path):
    anchors = set()
    seen = {}
    for _, line in content_lines(read(path)):
        heading = HEADING_RE.match(line)
        if heading:
            slug = github_slug(heading_text(heading.group(2)))
            unique = slug
            while unique in seen:
                seen[slug] += 1
                unique = "{}-{}".format(slug, seen[slug])
            seen[unique] = 0
            anchors.add(unique)
        anchors.update(HTML_ANCHOR_RE.findall(line))
    return frozenset(anchors)


@lru_cache(maxsize=None)
def page_anchors(path, _stack=()):
    anchors = set(own_anchors(path))
    for specifier in MACRO_IMPORT_RE.findall(read(path)):
        macro = os.path.join(ROOT, "macros", specifier[len("@macros/"):])
        if os.path.isfile(macro) and macro not in _stack:
            anchors |= page_anchors(macro, _stack + (path,))
    return frozenset(anchors)


def resolve_page(url_path):
    """Return the MDX file served at url_path, or None."""
    parts = [p for p in url_path.strip("/").split("/") if p]
    if parts and parts[0] == "tutorials":
        if len(parts) == 1:
            return None
        candidates = [os.path.join(ROOT, "tutorials", *parts[1:], "index.mdx")]
    else:
        base = os.path.join(ROOT, "pages", *parts)
        candidates = [os.path.join(base, "index.mdx"), base + ".mdx"]
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
    return None


def url_of(path):
    """Return the website path of an MDX file (used for relative links)."""
    rel = os.path.relpath(path, ROOT)[: -len(".mdx")].split(os.sep)
    if rel[-1] == "index":
        rel = rel[:-1]
    if rel[0] == "pages":
        rel = rel[1:]
    return "/" + "/".join(rel) + "/"


def is_file_link(url_path):
    return bool(os.path.splitext(url_path.rstrip("/"))[1])


def check_file_link(url_path, source):
    """Static files: relative to the source, in docs-content, or in the app's public/ dir."""
    rel = unquote(url_path).lstrip("/")
    candidates = []
    if not url_path.startswith("/"):
        candidates.append(os.path.join(os.path.dirname(source), rel))
    else:
        candidates.append(os.path.join(ROOT, rel))
        if rel.startswith("assets/"):
            candidates.append(os.path.join(ROOT, rel[len("assets/"):]))
        candidates.append(os.path.join(PUBLIC_DIR, rel))
    if any(os.path.exists(c) for c in candidates):
        return None
    if url_path.startswith("/") and not os.path.isdir(PUBLIC_DIR):
        return None  # cannot verify public assets outside the monorepo
    return "file not found"


def check_link(raw, source, check_anchors, check_slash):
    """Return an error message for a broken internal link, or None."""
    url = raw
    for prefix in DOCS_URL_PREFIXES:
        if url.startswith(prefix):
            url = url[len(prefix):] or "/"
            break
    else:
        if re.match(r"^[a-z][a-z0-9+.-]*:", url, re.I) or url.startswith("//"):
            return None  # external, mailto:, etc.
        if url.startswith("{") or "{" in url:
            return None  # JSX expression

    parts = urlsplit(url)
    path, fragment = parts.path, unquote(parts.fragment)

    if path and is_file_link(path):
        return check_file_link(path, source)

    if not path:
        target = source
    else:
        if not path.startswith("/"):
            if "macros" in os.path.relpath(source, ROOT).split(os.sep)[:1]:
                return "relative page link in a macro resolves differently on each page"
            path = os.path.normpath(os.path.join(url_of(source), path))
        segments = [s for s in path.split("/") if s]
        if "" == path.strip("/") or (len(segments) == 1 and segments[0] in APP_ROUTES):
            return None
        target = resolve_page(path)
        if target is None:
            return "page not found"
        if check_slash and not path.endswith("/"):
            return "missing trailing slash"

    if fragment and check_anchors:
        if fragment.endswith("/"):
            return "anchor has a trailing slash (#{})".format(fragment)
        if fragment not in page_anchors(target):
            return "anchor #{} not found in {}".format(fragment, os.path.relpath(target, ROOT))
    return None


def extract_links(line):
    scrubbed = INLINE_CODE_RE.sub("", line)
    links = MD_LINK_RE.findall(scrubbed) + HREF_RE.findall(scrubbed)
    ref = REF_LINK_RE.match(scrubbed)
    if ref:
        links.append(ref.group(1))
    # Absolute docs URLs written as plain text or inside JSX props
    for url in BARE_DOCS_URL_RE.findall(scrubbed):
        if url not in links:
            links.append(url)
    return links


def is_scanned(path):
    rel = os.path.relpath(path, ROOT).replace(os.sep, "/")
    return path.endswith(".mdx") and rel not in SKIP_FILES and not SKIP_FILE_RE.search(rel)


def iter_files(targets):
    for target in targets:
        target = os.path.abspath(target)
        if os.path.isfile(target):
            if is_scanned(target):
                yield target
            continue
        for dirpath, dirnames, filenames in os.walk(target):
            dirnames[:] = [d for d in dirnames if d not in ("node_modules", "assets")]
            for name in sorted(filenames):
                path = os.path.join(dirpath, name)
                if is_scanned(path):
                    yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("paths", nargs="*", help="files or directories to scan (default: pages, tutorials, macros, blocks, docs, changelog)")
    parser.add_argument("--no-anchors", action="store_true", help="do not check #anchors")
    parser.add_argument(
        "--trailing-slash",
        action="store_true",
        help="flag page links without a trailing slash (they work, through a redirect)",
    )
    args = parser.parse_args()

    targets = args.paths or [os.path.join(ROOT, d) for d in SCAN_DIRS]
    errors = 0
    files = 0
    for path in iter_files(targets):
        files += 1
        rel = os.path.relpath(path, ROOT)
        for number, line in content_lines(read(path)):
            for link in extract_links(line):
                message = check_link(link, path, not args.no_anchors, args.trailing_slash)
                if message:
                    errors += 1
                    print("{}:{}: {} -> {}".format(rel, number, link, message))

    print("\n{} broken link(s) in {} file(s) scanned.".format(errors, files), file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
