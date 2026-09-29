from __future__ import annotations

import re
from typing import Iterator, List, Tuple

from ..model import Check, Finding, Page

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LINK_RE = re.compile(r'(?<!!)\[([^\]]*)\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
FENCE_RE = re.compile(r"^\s*(```|~~~)")
BAD_LINK_TEXT = {"here", "this page", "this", "link", "click here", "this link"}
REQUIREMENTS_PAGE_TYPES = {"how-to", "quickstart", "tutorial"}
REQUIREMENTS_RE = re.compile(r"<Requirements\s*/>|^## Before you start", re.M)
INTERNAL_ABSOLUTE_RE = re.compile(r"^https?://(www\.)?scaleway\.com/en/docs/")


def prose_lines(page: Page) -> Iterator[Tuple[str, int]]:
    """Yields (text, 1-indexed file line) for body lines outside fenced code blocks."""
    in_fence = False
    for i, text in enumerate(page.body.split("\n")):
        if FENCE_RE.match(text):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield text, page.body_start_line + i


def check_headings(page: Page) -> List[Finding]:
    out: List[Finding] = []
    prev_level = 1  # H1 comes from the frontmatter title
    for text, line in prose_lines(page):
        m = HEADING_RE.match(text)
        if not m:
            continue
        level = len(m.group(1))
        title = m.group(2).strip()

        def add(check: str, severity: str, message: str) -> None:
            out.append(Finding(page.file, page.url, check, severity, message, line=line, evidence=title))

        if level == 1:
            add("structure/heading-h1", "error", "H1 in body; the title comes from frontmatter")
        elif level > prev_level + 1:
            add("structure/heading-skip", "warn", "H%d follows H%d; do not skip heading levels" % (level, prev_level))
        prev_level = level
    return out


def check_links(page: Page) -> List[Finding]:
    out: List[Finding] = []
    for text, line in prose_lines(page):
        for m in LINK_RE.finditer(text):
            label, href = m.group(1), m.group(2)

            def add(check: str, message: str) -> None:
                out.append(Finding(page.file, page.url, check, "warn", message, line=line, evidence=m.group(0)))

            if label.strip().lower() in BAD_LINK_TEXT:
                add("links/text", 'Non-descriptive link text "%s"' % label)
            if INTERNAL_ABSOLUTE_RE.match(href):
                add("links/internal-absolute", "Internal link uses absolute URL; use a relative path")
            elif href.startswith("/en/docs/"):
                add("links/internal-prefix", "Internal link must not include /en/docs/")
            elif href.startswith("/") and not href.startswith("//"):
                has_anchor = "#" in href
                path_part = href.split("#", 1)[0]
                if has_anchor and href.endswith("/"):
                    add("links/anchor-trailing-slash", "Anchor links must not end with a trailing slash")
                elif not has_anchor and not path_part.endswith("/"):
                    add("links/trailing-slash", "Internal links must end with a trailing slash")
            elif not re.match(r"^(https?:|mailto:|#)", href):
                add("links/relative", "Internal link must start with a leading slash")
    return out


def check_requirements(page: Page) -> List[Finding]:
    if page.page_type not in REQUIREMENTS_PAGE_TYPES or REQUIREMENTS_RE.search(page.body):
        return []
    return [Finding(page.file, page.url, "structure/requirements", "warn",
                    "%s pages should include the <Requirements /> macro" % page.page_type,
                    line=page.body_start_line)]


def run(pages: List[Page]) -> List[Finding]:
    return [f for p in pages for f in check_headings(p) + check_links(p) + check_requirements(p)]


CHECK = Check("structure", run)
