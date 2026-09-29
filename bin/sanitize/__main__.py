"""
Doc sanitize suite. Run from the docs-content root:

    python -m bin.sanitize                          # whole corpus
    python -m bin.sanitize --product kubernetes     # one product
    python -m bin.sanitize pages/vpc/faq.mdx        # specific files
    python -m bin.sanitize tutorials pages/vpc/how-to   # directories (recursive)
    python -m bin.sanitize --changed --fail-on error    # files changed vs origin/main (CI on PRs)
    python -m bin.sanitize --checks frontmatter,structure
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from typing import List, Optional

from .checks import frontmatter, structure, vale, versions
from .corpus import PAGES_DIR, TUTORIALS_DIR, load_corpus, walk_mdx
from .model import SEVERITY_WEIGHT, Check, Finding
from .report import format_console, write_report

CHECKS: List[Check] = [frontmatter.CHECK, structure.CHECK, versions.CHECK, vale.CHECK]
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "report")


def changed_files() -> List[str]:
    """Changed .mdx files under pages/ and tutorials/ only, so a PR cannot point the tool at arbitrary paths."""
    base = subprocess.check_output(["git", "merge-base", "HEAD", "origin/main"], text=True).strip()
    out = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=ACMR", base, "--",
         PAGES_DIR + "/*.mdx", TUTORIALS_DIR + "/*.mdx"],
        text=True,
    )
    return [line for line in out.splitlines() if line]


def expand_paths(paths: List[str]) -> Optional[List[str]]:
    """Files stay as given; directories expand to the .mdx files under them. Empty -> None (whole corpus)."""
    if not paths:
        return None
    out: List[str] = []
    for p in paths:
        out.extend(walk_mdx(p) if os.path.isdir(p) else [p])
    return out


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="sanitize", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("files", nargs="*", help=".mdx files or directories to scan (default: whole corpus)")
    parser.add_argument("--product", help="only pages of this product slug (e.g. kubernetes)")
    parser.add_argument("--changed", action="store_true", help="only .mdx files changed vs origin/main")
    parser.add_argument("--checks", default=",".join(c.name for c in CHECKS), help="comma-separated check names")
    parser.add_argument("--fail-on", choices=list(SEVERITY_WEIGHT), help="exit 1 if any finding reaches this severity")
    parser.add_argument("--quiet", action="store_true", help="no per-check timing on stderr")
    args = parser.parse_args(argv)

    files = changed_files() if args.changed else expand_paths(args.files)
    pages = load_corpus(product=args.product, files=files)
    wanted = set(args.checks.split(","))
    findings: List[Finding] = []
    for check in (c for c in CHECKS if c.name in wanted):
        started = time.time()
        result = check.run(pages)
        findings.extend(result)
        if not args.quiet:
            print("%s: %d findings (%.0f ms)" % (check.name, len(result), (time.time() - started) * 1000),
                  file=sys.stderr)

    write_report(findings, len(pages), OUT_DIR)
    print(format_console(findings, len(pages)))
    print("\nReport written to %s/findings.{md,json,csv}" % os.path.relpath(OUT_DIR))

    if args.fail_on and any(SEVERITY_WEIGHT[f.severity] >= SEVERITY_WEIGHT[args.fail_on] for f in findings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
