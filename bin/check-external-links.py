#!/usr/bin/env python3
"""Check external links in docs-content MDX files with lychee.

Wraps lychee (https://lychee.cli.rs) with the docs-content config below, and
also checks URLs in JSX props (url="...", src="..."), which lychee does not
read: they are extracted to temporary Markdown files checked alongside the MDX.

Requires lychee: brew install lychee (or cargo install lychee).
Set GITHUB_TOKEN to avoid GitHub rate limits (defaults to `gh auth token`).

Usage (from anywhere in the repository):
    python3 bin/check-external-links.py                    # pages/, tutorials/, macros/, changelog/
    python3 bin/check-external-links.py pages/instances    # a subset
    python3 bin/check-external-links.py pages/ --accept '200..=299, 403, 429'

Arguments that are existing files or directories are scanned; all other
arguments are passed to lychee as is.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCAN_DIRS = ("pages", "tutorials", "macros", "changelog")

FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
JSX_PROP_URL_RE = re.compile(r"""\b(?:url|src)=\{?["'](https?://[^"'}\s]+)""")

# https://lychee.cli.rs/config/ (paths are relative to the docs-content root)
CONFIG = r"""
max_concurrency = 32
host_concurrency = 4
max_retries = 2
retry_wait_time = 2
timeout = 20

# Successful results are cached in .lycheecache; failures are always rechecked
cache = true
max_cache_age = "3d"
cache_exclude_status = "400..=599"

# 429: rate limited, the page exists
accept = ["200..=299", "429"]

scheme = ["https", "http"]

# Internal docs links are covered by bin/check-internal-links.py.
# Root-relative and relative links resolve against this placeholder, then get excluded.
base_url = "https://internal.invalid/"
exclude = [
  '^https?://internal\.invalid',
  '^https?://www\.scaleway\.com/en/docs',
  '^https?://virtualmedia\.online\.net',
  '^https?://www\.scaleway\.com/(en|fr)(/|$)',
  # Behind login or invite-only
  '^https?://console\.scaleway\.com',
  '^https?://account\.scaleway\.com',
  '^https?://console\.online\.net',
  '^https?://slack\.scaleway\.com',
  '^https?://([a-z0-9-]+\.)?slack\.com',
  # API endpoints shown as examples
  '^https?://api\.scaleway\.(com|ai)',
  '\.scw\.cloud',
  '\.scw\.dev',
  # Placeholders
  '<[^>]+>',
  '\{[^}]*\}',
  '\$\{?[A-Z_]',
  '^https?://(www\.)?example\.(com|org|net)',
  '\.example\.(com|org|net)',
  '^https?://(localhost|127\.0\.0\.1|0\.0\.0\.0)',
  'your-domain',
]
exclude_private = true
exclude_link_local = true
exclude_loopback = true

# Style guide and templates contain example links
exclude_path = ['pages/guidelines\.mdx', 'TEMPLATE.*\.mdx$', 'docs/templates/']
"""


def iter_mdx(paths):
    for path in paths:
        if os.path.isfile(path):
            if path.endswith(".mdx"):
                yield path
            continue
        for dirpath, dirnames, filenames in os.walk(path):
            dirnames[:] = [d for d in dirnames if d not in ("node_modules", "assets")]
            for name in sorted(filenames):
                if name.endswith(".mdx"):
                    yield os.path.join(dirpath, name)


def extract_jsx_prop_urls(inputs, out_dir):
    """Write URLs found in JSX props to <out_dir>/<source file>.md, outside code blocks."""
    for path in iter_mdx(inputs):
        with open(path, encoding="utf-8", errors="replace") as f:
            lines = f.read().split("\n")
        found = []
        in_fence = False
        for number, line in enumerate(lines, start=1):
            if FENCE_RE.match(line):
                in_fence = not in_fence
            elif not in_fence:
                found += ["- line {}: <{}>".format(number, url) for url in JSX_PROP_URL_RE.findall(line)]
        if found:
            # Inputs outside ROOT (../x) use their absolute path, to stay inside out_dir
            name = os.path.abspath(path).lstrip(os.sep) if path.startswith("..") else path
            target = os.path.join(out_dir, name + ".md")
            os.makedirs(os.path.dirname(target), exist_ok=True)
            with open(target, "w", encoding="utf-8") as f:
                f.write("\n".join(found) + "\n")


def github_token():
    if os.environ.get("GITHUB_TOKEN") or not shutil.which("gh"):
        return os.environ.get("GITHUB_TOKEN")
    result = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
    return result.stdout.strip() or None


def main():
    lychee = shutil.which("lychee")
    if not lychee:
        print("lychee is not installed: brew install lychee (or cargo install lychee)", file=sys.stderr)
        return 2

    inputs, options = [], []
    for arg in sys.argv[1:]:
        if os.path.exists(arg):
            inputs.append(os.path.relpath(os.path.abspath(arg), ROOT))
        else:
            options.append(arg)
    inputs = inputs or list(SCAN_DIRS)

    env = dict(os.environ)
    token = github_token()
    if token:
        env["GITHUB_TOKEN"] = token

    with tempfile.TemporaryDirectory() as tmp:
        config = os.path.join(tmp, "lychee.toml")
        with open(config, "w", encoding="utf-8") as f:
            f.write(CONFIG)
        props_dir = os.path.join(tmp, "jsx-props")
        os.makedirs(props_dir)
        # Relative paths so the report and exclude_path match docs-content paths
        os.chdir(ROOT)
        extract_jsx_prop_urls(inputs, props_dir)
        command = [lychee, "--config", config, "--no-progress"] + options + inputs + [props_dir]
        return subprocess.run(command, env=env).returncode


if __name__ == "__main__":
    sys.exit(main())
