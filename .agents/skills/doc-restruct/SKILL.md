---
name: doc-restruct
description: Restructures a scaleway/docs-content section from type-based folders (how-to, reference-content...) to topic-based folders — migrates pages, fixes internal links, and prepares the redirect handoff.
---

# doc-restruct

Pointer guide for restructuring a documentation section in **scaleway/docs-content**, generalized from the IAM / Account / Organizations and Projects restructuring (PR #6877). The goal is to automate the mechanical, error-prone parts — mapping, migration, link-fixing, redirect handoff — while keeping the judgment calls (new architecture, `menu.ts` changes, redirect timing) as explicit human checkpoints. Skipping those checkpoints is how a restructuring silently breaks navigation or SEO.

**Reference implementation**: PR #6877, sections `account/`, `iam/`, `organizations-and-projects/`. See also the `AGENTS.md` and `llms.txt` for repo structure, protected directories, and writing conventions — read it before touching any file in scope.

---

## Step 1 — Select the section(s) to restructure

Ask the user which top-level entry in `menu/navigation.ts` is being restructured (e.g. "Security & Identity", "Instances"), then confirm which product folders in `pages/` are in scope (e.g. `account`, `iam`, `organizations-and-projects`).

## Step 2 — Get the validated mapping

**This skill does not design the new architecture.** The new folder structure is decided upstream, by the user with the doc team (typically worked out on a shared Figma board) — that decision, and its validation, happens before this skill is used.

1. Ask the user for the final old → new path mapping (e.g. a CSV, or a table like the one produced for PR #6877), already validated with the team.
2. Treat it as a fixed input for the rest of this skill — do not second-guess or re-propose the structure. If the mapping looks incomplete or inconsistent (a page in scope with no listed destination, a conflict), flag it to the user rather than resolving it by inference.
3. Do not move to Step 3 until a complete, validated mapping is in hand.

## Step 3 — Migrate the files

This step runs automatically from the validated mapping (Step 2) — at this scale (1,150+ files for IAM/Account/Organizations), moving files one by one is not practical. Automation is safe here specifically because it's checked immediately after, not because the mapping is assumed correct.

1. Before touching anything, validate the mapping itself: every `old_path` exists in the repo, every `new_path` is unique (no two sources mapping to the same destination), and no entry is malformed (empty field, relative path escaping `pages/`). Stop and report instead of running if any of this fails.
2. For every entry, run `git mv old_path new_path` — never delete + recreate. `git diff -M` (rename detection) is what Step 4 relies on to confirm the mapping was applied correctly; losing that history makes the link fix much harder to verify.
3. Only touch a moved page's frontmatter (`categories`, breadcrumbs) if the move itself changes it — never touch content in this step.
4. Immediately after, diff the actual `git mv` operations (`git diff -M --summary`) against the Step 2 mapping, entry by entry: every mapped file was moved, nothing extra moved, nothing was missed. Report any mismatch before continuing — do not proceed to Step 4 with an unverified migration.
5. Export the confirmed mapping as `old_url,new_url` CSV — Steps 4, 5, and 6 all reuse it.

## Step 4 — Fix internal links

Goal: fix every broken internal documentation link caused by the move, repo-wide.

**Source of truth**
- Build the mapping from `git diff -M` (Step 3), not by guessing. Don't invent a mapping for a link to a page that was deleted with no successor — flag those for manual review instead.
- Normalize it: keep trailing slashes only where the original relative link already had one; preserve `#anchors` and `?query` strings exactly (e.g. `.../?tab=log-in-with-sso-0`).

**Scope**
- All `.mdx`, `.ts`, `.json`, and other text files (`.md`, `.yml`, `.yaml`, `.txt`, extension-less MDX) across the repo: `pages/`, `macros/`, `tutorials/`, and — only with explicit user confirmation, since they're protected directories — `changelog/`, `menu/`, `blocks/`.
- Scan the current working tree, not a stale snapshot, and re-scan after applying: merges or later commits can reintroduce old links.

**Guardrails — must NOT be rewritten**
- Console URLs (`https://console.scaleway.com/...`).
- API endpoint paths (`/iam/v1alpha1/...`, `/account/v3/...`).
- Macro imports / component paths (`@macros/iam/requirements.mdx`).
- Sibling products that share a slug fragment but didn't move (e.g. `dedibox-account/` must never match a rename of `account`) — anchor the product slug as a full path segment, not a substring.
- No double-remap: verify nothing becomes `glossary/glossary` or `quickstart/quickstart`.

**Execution**
1. Dry run first: print every proposed `- old` / `+ new` line, a per-file summary, and an "unmatched token" list for review.
2. Review the unmatched tokens — confirm they're all guardrail cases, not skipped real links.
3. Apply the edits.
4. Re-run the dry run — it must report **0 remaining replacements**.
5. Grep the whole repo for leftover old-path references (excluding console/API) — must be **0**.
6. Spot-check diffs across each touched directory: anchors, query strings, and EOF newlines preserved.

**Acceptance criteria**: 0 old links left anywhere in scope; every rewritten link resolves to a page that exists; no guardrail case touched; the old → new CSV mapping is up to date with what was actually applied.

## Step 5 — Update navigation (human checkpoint)

⚠️ `menu/` is a protected directory — never edit `menu.ts` / `navigation.ts` automatically. Propose the new menu entries as a diff for the user to review, and apply it only after explicit per-file confirmation.

## Step 6 — Hand off redirects to the Website team

1. Share the `old_url,new_url` CSV with the Website team so they can set up a redirection script covering the transition period — this is what keeps old links working while references across the console, support, and marketing content get updated.
2. Flag explicitly whether anchors/query strings in the mapping need special handling on their side.
3. Track the script as temporary: plan its removal once every internal reference points to the new URLs (tie this to Step 9's deliverables, not left implicit).

## Step 7 — Clean up unused assets

Grep `assets/` and product-level image folders for files no longer referenced after the move. List them for the user to confirm — don't delete automatically; an image can be referenced from a macro or a page outside the restructured scope.

## Step 8 — Deploy a preview and verify

Deploy a preview environment for cross-review before opening the PR. Checklist before requesting review:

- [ ] Dry-run link fix re-run = 0 remaining replacements
- [ ] Repo-wide grep for old paths = 0 (excluding console/API URLs)
- [ ] No orphaned double-remaps (`glossary/glossary`, `quickstart/quickstart`...)
- [ ] Preview reviewed by the doc team
- [ ] Redirect script confirmed live with the Website team

## Step 9 — Deliverables

- Old → new URL mapping (CSV), kept as the single source of truth for Steps 4, 5, and 6.
- Summary of files changed by directory and total replacements.
- Validation report: dry-run recheck, grep recheck, and any manually-handled edge case (deleted section-index pages, `?query` links, extension-less files).

---

## Gaps this skill will NOT catch automatically

- **Final architecture** — always a human decision, validated with the doc team (Step 2).
- **`menu.ts` / `navigation.ts` changes** — protected directory, human-applied (Step 5).
- **Redirect script implementation** — owned by the Website team, not generated here (Step 6).
- **SEO re-indexation timeline** — owned by SEO stakeholders, monitored after merge, not predicted here.