# Docs sanitize suite

Analyzes the MDX corpus (`pages/` and `tutorials/`) against a set of checks and writes a ranked report. Every check implements the same `Check` interface and emits `Finding` objects in a common schema, so new analyzers plug in without touching the reporting layer.

Python 3.9+, stdlib plus `pyyaml`. Tests with `pytest`. Prose checks use the [Vale](https://vale.sh) binary.
Dependencies are pinned in [requirements.txt](requirements.txt), kept separate from the root one (which belongs to `bin/check-review-dates.py`).

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

No venv activation needed: the pnpm scripts call `bin/sanitize/.venv/bin/python` directly. Everything the suite generates (venv, caches, reports) stays under `bin/sanitize/` and is gitignored there; nothing is added at the repo root.

Output goes to `bin/sanitize/report/` (gitignored):

| File            | Purpose |
| --------------- | ------- |
| `findings.md`   | Human-readable. Summary table, then one section per file, one line per finding. Read this one. |
| `findings.json` | Grouped by file (`files[] -> findings[]`), files sorted by score. For tooling. |
| `findings.csv`  | Flat, one row per finding. For spreadsheets. Cells starting with `=`, `+`, `-`, `@`, tab or CR are prefixed with `'` so page content cannot inject formulas (`csv_cell()` in `report.py`). |

The console prints the same content as `findings.md`. `--fail-on error|warn|info` exits 1 if any finding reaches that severity; otherwise the exit code is always 0.

## What is checked

### `frontmatter` — [checks/frontmatter.py](checks/frontmatter.py)

| Check id                         | Severity   | Rule |
| -------------------------------- | ---------- | ---- |
| `frontmatter/required`           | error/warn | `title`, `description`, `dates.validation` (error); `tags` (warn). Landing pages (`index.mdx`) only need title + description. |
| `frontmatter/description-length` | info       | 120–160 chars (SEO guideline). |
| `frontmatter/title`              | warn/info  | How-to titles start with "How to" (warn), ≤ 5 words after it (info); tutorial titles start with a gerund (info). |
| `frontmatter/date-format`        | error      | `dates.*` must be `yyyy-mm-dd`. |
| `frontmatter/date-order`         | error      | `validation` ≥ `posted`. |
| `frontmatter/date-future`        | error      | `validation` not in the future. |
| `frontmatter/stale`              | warn/error | **Disabled** (`ENABLE_STALE_CHECK = False`): review-date policy is not enforced yet. When enabled: overdue vs `validation_frequency` (default 6 months, same as `bin/check-review-dates.py`); error at 2× overdue. |

### `structure` — [checks/structure.py](checks/structure.py)

Skips fenced code blocks.

| Check id                      | Severity | Rule |
| ----------------------------- | -------- | ---- |
| `structure/heading-h1`        | error    | No `#` in body; the H1 is the frontmatter title. |
| `structure/heading-skip`      | warn     | No skipped levels (H2 → H4). |
| `structure/heading-case`      | info     | Title Case heuristic (≥ 60 % of following words capitalized). |
| `structure/requirements`      | warn     | how-to, quickstart and tutorial pages must contain `<Requirements />` or `## Before you start`. |
| `links/text`                  | warn     | Link text is not "here", "this page", … |
| `links/trailing-slash`        | warn     | Internal links end with `/`. |
| `links/anchor-trailing-slash` | warn     | Anchor links (`/x/#y`) do **not** end with `/`. |
| `links/internal-absolute`     | warn     | No `https://www.scaleway.com/en/docs/...` for internal links. |
| `links/internal-prefix`       | warn     | No `/en/docs/` prefix. |
| `links/relative`              | warn     | Internal links start with `/`. |

### `versions` — [checks/versions.py](checks/versions.py)

Flags software versions past end-of-life per [endoflife.date](https://endoflife.date). Scans prose **and** code blocks (image tags, `apt install` lines). Products tracked: Ubuntu, Debian, Kubernetes, Python, Node.js, PHP, Go, PostgreSQL, MySQL, Terraform, Windows Server, Rocky Linux, AlmaLinux, CentOS — see `PATTERNS` to add one (endoflife.date slug + regex with the cycle in group 1).

| Check id            | Severity  | Rule |
| ------------------- | --------- | ---- |
| `versions/eol`      | warn/info | Version is past EOL. One finding per page per version, with mention count. Downgraded to `info` when every mention sits on a line that already says "end of life", "EOL", "deprecated" or "not supported" (pages that list retired runtimes on purpose). |
| `versions/eol-soon` | info      | EOL within 90 days. |

Unknown cycles (typos, versions not tracked) are silent on purpose. API responses are cached 7 days in `bin/sanitize/.cache/endoflife/` (gitignored); offline, a stale cache is used, otherwise the product is skipped with a warning.

### `vale` — [checks/vale.py](checks/vale.py) + [vale/.vale.ini](vale/.vale.ini)

Prose rules from the [writing guidelines](https://www.scaleway.com/en/docs/guidelines/), as Vale styles in `vale/styles/Scaleway/`. Reported as `vale/<Style>.<Rule>`.

| Rule                       | Level      | What |
| -------------------------- | ---------- | ---- |
| `Scaleway.BritishSpelling` | warning    | colour → color, etc. |
| `Scaleway.Contractions`    | warning    | can't → cannot, etc. |
| `Scaleway.Tone`            | warning    | please / thank you. |
| `Scaleway.ClickOn`         | warning    | "click on" → "click". |
| `Scaleway.Possessive`      | warning    | `Instance's`, `Scaleway's`, … |
| `Scaleway.Pronouns`        | suggestion | we / our / the user. |
| `Scaleway.FutureTense`     | suggestion | "will open", "will be created", … |
| `Scaleway.Passive`         | suggestion | "is created by", … |
| `Scaleway.HeadingCase`     | suggestion | Sentence-case headings; product names listed as `exceptions`. |

Vale level → suite severity: error → `error`, warning → `warn`, suggestion → `info`.

**Spelling is deliberately not checked here.** `Vale.Spelling` produced ~10k alerts on the corpus, nearly all product and tool names (Dedibox, Nginx, systemd, …) that cannot be whitelisted without a huge dictionary, and typo detection is already covered by [typos](https://github.com/crate-ci/typos). `Vale.Spelling` and `Vale.Terms` are set to `NO` in `.vale.ini`; `accept.txt` only feeds the remaining style rules. Heading false positives go into `HeadingCase.yml` exceptions. Run Vale alone on a folder to iterate quickly: `vale --config bin/sanitize/vale/.vale.ini pages/block-storage/`.

## Ranking

Each finding scores error 3, warn 2, info 1. A file's score is the sum of its findings; files are listed worst first. Page-view analytics were considered as a multiplier (so high-traffic pages rank first) and dropped for now; if revisited, `score()` in `report.py` is the single place to change.

## Layout

```
bin/sanitize/
  __main__.py          CLI, check registry (CHECKS), --changed via git diff
  corpus.py            loads MDX -> Page(file, url, product, page_type, frontmatter, body, body_start_line, hash)
  model.py             Page, Finding, Check, severity weights, page types
  report.py            score, group_by_file, console / markdown / JSON / CSV writers
  checks/
    frontmatter.py
    structure.py
    versions.py
    vale.py
  tests/test_sanitize.py   pytest: URL mapping, classification, frontmatter parsing, every check, ranking
  requirements.txt         pyyaml, pytest (this suite only)
  vale/.vale.ini
  vale/styles/Scaleway/*.yml
  vale/styles/config/vocabularies/Scaleway/{accept,reject}.txt
  .gitignore               ignores the generated dirs below
  .venv/                   created by pnpm sanitize:setup
  .cache/endoflife/        endoflife.date responses
  report/                  findings.{md,json,csv}
```

URL mapping: `pages/kubernetes/how-to/create-cluster.mdx` → `/kubernetes/how-to/create-cluster/`, `pages/x/index.mdx` → `/x/`, `tutorials/strapi/index.mdx` → `/tutorials/strapi/`. Page type is the second URL segment (`how-to`, `concepts`, …), `index` for any `index.mdx`, `tutorial` for tutorials, `other` for anything else (e.g. `videos.mdx`).

## Adding a check

```python
# bin/sanitize/checks/my_check.py
from ..model import Check, Finding, Page

def check_my_thing(page: Page) -> list:
    return [Finding(page.file, page.url, "my/thing", "warn", "message", line=12, evidence="...")]

CHECK = Check("my-check", lambda pages: [f for p in pages for f in check_my_thing(p)])
```

Register it in `CHECKS` in `__main__.py`, add tests in `tests/test_sanitize.py`. `page.hash` (sha1 of the raw file) is there for checks that are expensive to run: cache results keyed by hash so unchanged pages are skipped.

## Roadmap

Done: corpus, report, frontmatter, structure, Vale, versions (endoflife.date).

Considered and set aside:

- **Spelling** — see above; handled by [typos](https://github.com/crate-ci/typos) instead.
- **Page-view analytics (Amplitude)** as a ranking multiplier — needs credentials, and traffic data should not land in a public repo.
- **Scaleway deprecations from `changelog/`** — changelog titles are too heterogeneous for automatic keyword extraction; a deterministic version would need a hand-curated terms file.
- **LLM checks** (obsolescence vs changelog, cross-page consistency, soft writing guidelines) — need an API key and a run budget. If revisited: structured JSON output, cached by `page.hash`, findings feed a review queue and never auto-fix.

Run modes once complete: PR CI (`--changed --fail-on error`), weekly full run pushed to Slack (like `bin/check-review-dates.py`), on-demand per product.

## Decisions log

- Python, not TypeScript: the suite lives in docs-content, which already has Python tooling (`bin/check-review-dates.py`, `requirements.txt`) and no TS toolchain.
- Prose rules live in Vale, not Python: it handles code-block skipping, suggestions and vocab natively. Python handles what Vale cannot see (frontmatter, heading hierarchy, link format, page-type rules).
- Everything the suite owns lives under `bin/sanitize/`, including the Vale config, its own pinned `requirements.txt` and all generated files, so the repo root stays clean and the Slack script's deps stay separate.
- `frontmatter/stale` disabled by flag rather than removed: the logic mirrors the existing review-date script and is ready when the policy is enforced.
- `Vale.Terms` disabled: it turned vocab entries into casing rules and produced false errors (`rsync` vs `Rsync`).
- Heading-case and gerund-title checks are heuristics, so they are `info` only.
- `--changed` is restricted to `pages/**` and `tutorials/**` so a PR cannot point the tool at arbitrary paths.
- Page content is treated as untrusted (the repo takes external PRs): frontmatter goes through `yaml.safe_load`, subprocess calls use argument lists with `./`-prefixed paths, and CSV cells are escaped against spreadsheet formula injection.
