# Docs sanitize suite

Analyzes the MDX corpus (`pages/` and `tutorials/`) against a set of checks and writes a ranked report. Every check implements the same `Check` interface and emits `Finding` objects in a common schema, so new analyzers plug in without touching the reporting layer.

Python 3.9+, stdlib plus `pyyaml`. Tests with `pytest`. Prose checks use the [Vale](https://vale.sh) binary.

## Setup

```bash
pnpm sanitize:setup      # venv in bin/sanitize/.venv + deps from bin/sanitize/requirements.txt
brew install vale        # optional; prose checks are skipped with a warning if missing
```

## Usage

Run from the docs-content root.

```bash
pnpm sanitize                              # whole corpus (~2,000 pages, ~1 s without Vale)
pnpm sanitize --product block-storage      # pages/<product>/ + tutorials with products: [<product>]
pnpm sanitize pages/vpc/faq.mdx            # one or more specific files
pnpm sanitize tutorials pages/vpc/how-to   # directories, recursive
pnpm sanitize --changed --fail-on error    # .mdx files changed vs origin/main (CI on PRs)
pnpm sanitize --checks frontmatter,structure
pnpm sanitize --quiet                      # no per-check timing on stderr
pnpm sanitize:test
```

No venv activation needed: the pnpm scripts call `bin/sanitize/.venv/bin/python` directly. Everything the suite generates (venv, caches, reports) stays under `bin/sanitize/`.

Output is `bin/sanitize/report/findings.md`

