#!/usr/bin/env python3
"""Report macros that are never used, or used by a single file.

A macro counts as used by a file when that file imports it
(import X from '@macros/...mdx') and renders it (<X />). Imports that are
never rendered are reported separately, as are imports of missing macros
and macros rendered several times in the same file.

Usage (from the docs-content root):
    python3 bin/check-macro-usage.py           # unused and single-use macros
    python3 bin/check-macro-usage.py --unused  # unused macros only

Exits with status 1 when unused macros or broken imports are found.
"""
import argparse
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MACROS_DIR = os.path.join(ROOT, "macros")
SCAN_DIRS = ("pages", "tutorials", "macros", "blocks", "docs", "changelog")
# Style guide and templates show example usage, not real content
SKIP_FILES = {"pages/guidelines.mdx"}
SKIP_FILE_RE = re.compile(r"(TEMPLATE.*\.mdx$|^docs/templates/)")
# Macros meant to be rendered once per section or tab
REPEATABLE_MACROS = {"iam/requirements.mdx"}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
IMPORT_RE = re.compile(r"""^import\s+(\w+)\s+from\s+["'](@macros/[^"']+)["']""")


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, "/")


def iter_mdx(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        dirnames[:] = [d for d in dirnames if d not in ("node_modules", "assets")]
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            if name.endswith(".mdx") and rel(path) not in SKIP_FILES and not SKIP_FILE_RE.search(rel(path)):
                yield path


def parse(path):
    """Return ({component: specifier}, text outside code fences) for an MDX file."""
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().split("\n")
    imports = {}
    body = []
    in_fence = False
    for line in lines:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = IMPORT_RE.match(line)
        if match:
            imports[match.group(1)] = match.group(2)
        else:
            body.append(line)
    return imports, "\n".join(body)


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--unused", action="store_true", help="only report unused macros")
    args = parser.parse_args()

    users = {path: set() for path in iter_mdx(MACROS_DIR)}
    unrendered = []
    missing = []
    repeated = []
    for directory in SCAN_DIRS:
        for path in iter_mdx(os.path.join(ROOT, directory)):
            imports, body = parse(path)
            for component, specifier in imports.items():
                macro = os.path.normpath(os.path.join(MACROS_DIR, specifier[len("@macros/"):]))
                if macro not in users:
                    missing.append((path, specifier))
                    continue
                renders = len(re.findall(r"<{}[\s/>]".format(component), body))
                if not renders:
                    unrendered.append((path, specifier))
                    continue
                users[macro].add(path)
                if renders > 1 and rel(macro)[len("macros/"):] not in REPEATABLE_MACROS:
                    repeated.append((path, specifier, renders))

    unused = sorted(m for m, u in users.items() if not u)
    single = sorted(m for m, u in users.items() if len(u) == 1)

    print("Unused macros ({}):".format(len(unused)))
    for macro in unused:
        print("  " + rel(macro))
    if not args.unused:
        print("\nMacros used by a single file ({}):".format(len(single)))
        for macro in single:
            print("  {} <- {}".format(rel(macro), rel(next(iter(users[macro])))))
    if unrendered:
        print("\nImported but never rendered ({}):".format(len(unrendered)))
        for path, specifier in unrendered:
            print("  {}: {}".format(rel(path), specifier))
    if repeated:
        print("\nRendered several times in the same file ({}):".format(len(repeated)))
        for path, specifier, renders in repeated:
            print("  {}: {} ({}x)".format(rel(path), specifier, renders))
    if missing:
        print("\nImports of missing macros ({}):".format(len(missing)))
        for path, specifier in missing:
            print("  {}: {}".format(rel(path), specifier))

    return 1 if unused or missing else 0


if __name__ == "__main__":
    sys.exit(main())
