---
name: doc-restruct
description: Restructures a scaleway/docs-content section from type-based folders (how-to, reference-content...) to topic-based folders — migrates pages, fixes internal links, and prepares the redirect handoff.
---

# doc-restruct

Pointer guide for restructuring a documentation section in **scaleway/docs-content**, generalized from the IAM / Account / Organizations and Projects restructuring (PR #6877). The goal is to automate the mechanical, error-prone parts — mapping, migration, link-fixing, redirect handoff — while keeping the judgment calls (new architecture, `menu.ts` changes, redirect timing) as explicit human checkpoints. Skipping those checkpoints is how a restructuring silently breaks navigation or SEO.

**Reference implementation**: PR #6877, sections `account/`, `iam/`, `organizations-and-projects/`. See also the `AGENTS.md` and `llms.txt` for repo structure, protected directories, and writing conventions — read it before touching any file in scope.

---

## Progress reports (debugging aid)

At the end of every step, before starting the next one, the agent writes a short report so the user can see what happened and where the run stands, and so a failure can be located quickly. Use this format:

```
Step N — <name>: <done | blocked | needs your decision>
Did: what was actually executed (commands run, files touched, counts)
Found: anything unexpected (mismatches, skipped entries, warnings)
Next: the next step, or what is needed from the user to continue
```

Rules:
- Report counts, not impressions: files moved, links rewritten, redirect lines generated, entries skipped.
- Report what was skipped or flagged as well as what succeeded. An empty "Found" must say "nothing unexpected", not be left out.
- When a step fails or stops on a validation, say which check failed and on which entries, and stop there rather than moving on.
- After Step 8, give one final status table: each step with its state and its key number.

---

## Step 1 — Select the section(s) to restructure

Ask the user which top-level entry in `menu/navigation.ts` is being restructured (e.g. "Security & Identity", "Instances"), then confirm which product folders in `pages/` are in scope (e.g. `account`, `iam`, `organizations-and-projects`).

**Report: the section and product folders confirmed as in scope.**

## Step 2 — Get the validated mapping

**This skill does not design the new architecture.** The new folder structure is decided upstream, by the user with the doc team (typically worked out on a shared Figma board) — that decision, and its validation, happens before this skill is used.

1. Ask the user for the final old → new path mapping (e.g. a CSV, or a table like the one produced for PR #6877), already validated with the team.
2. Treat it as a fixed input for the rest of this skill — do not second-guess or re-propose the structure. If the mapping looks incomplete or inconsistent (a page in scope with no listed destination, a conflict), flag it to the user rather than resolving it by inference.
3. Do not move to Step 3 until a complete, validated mapping is in hand.

**Report: number of entries in the mapping, and any entry flagged as incomplete or inconsistent.**

## Step 3 — Migrate the files

This step runs automatically from the validated mapping (Step 2) — at this scale (1,150+ files for IAM/Account/Organizations), moving files one by one is not practical. Automation is safe here specifically because it's checked immediately after, not because the mapping is assumed correct.

1. Before touching anything, validate the mapping itself: every `old_path` exists in the repo, every `new_path` is unique (no two sources mapping to the same destination), and no entry is malformed (empty field, relative path escaping `pages/`). Stop and report instead of running if any of this fails.
2. For every entry, run `git mv old_path new_path` — never delete + recreate. `git diff -M` (rename detection) is what Step 4 relies on to confirm the mapping was applied correctly; losing that history makes the link fix much harder to verify.
3. **Move the images with their pages.** Images sit in an `assets/` folder next to the pages that use them, so a page moved to a new folder needs its images in that folder's `assets/`. First confirm the convention on one existing page of the section (how its images are referenced: relative `assets/...` path, or another form); if it differs from what is described here, stop and ask the user. Then, for every moved page:
   - List the images it references. For each one, `git mv` it from the old folder's `assets/` to the new folder's `assets/` (create it if needed), keeping the file name, so the relative links in the page stay valid and the page content needs no change.
   - If an image is referenced by several pages that end up in different folders, copy it into each destination `assets/` (`git mv` for the first, `cp` for the others) rather than rewriting links to a shared location. The original is left in place if something still references it; Step 7 lists what ends up unused.
   - If an image is referenced by a macro, by a page outside the moved set, or by a path that points to the root `assets/`, do not move it: add it to a list for the user. The root `assets/` folder is protected and is only edited with the user's explicit confirmation.
   - Never rename an image and never delete one in this step.
4. **Create an `index.mdx` for every new folder** (content under `pages/` is in the allowed scope). For each new folder:
   - **Format**: a folder `index.mdx` contains only a frontmatter with `title` and `description`, and no body, as in this example:

     ```mdx
     ---
     title: Login and credentials
     description: Understand how to log in to your Scaleway account and manage your credentials.
     ---
     ```

     Do not add `tags`, `dates` or `categories`. Never add `draftedBy` (or any other agent attribution) to any page this skill creates or edits, even though the repo's general rule asks for it on agent-written content: this is the user's explicit choice for this skill. Before writing, check one existing folder `index.mdx` of the section in case the format has changed, and mirror it if so, still without `draftedBy`.
   - **Title**: the new folder's title in sentence case, taken from the validated architecture of Step 2. If Step 2 gave no titles, propose them and wait for the user's confirmation before writing. The same label is reused in `menu.ts` in Step 5, so keep them identical.
   - **Description (SEO)**, written in American English, present tense, active voice, following these rules:
     - Front-load the primary keywords: put the key terms (for example "manage IAM policies", "Scaleway Web Hosting") within the first 50 characters.
     - Include one or two actionable subtopics (for example create, configure, delete) to match long-tail search queries.
     - Total length between 120 and 155 characters, spaces included, so Google does not truncate the snippet.
     - Example shape: `Manage IAM policies and permission sets on Scaleway: create policies, configure rule conditions, and review access for users and groups.` (that example is 136 characters).
   - **Check each description by script**: character count between 120 and 155, and a primary keyword inside the first 50 characters. Rewrite any that fail instead of listing them as exceptions.
   - Write the list of folders with their title, description and character count to the report so the user can review them in one table. Index files are created in the same commit as the moves, never modify the moved pages to link to them.
5. Only touch a moved page's frontmatter (`categories`, breadcrumbs) if the move itself changes it — never touch the rest of the content in this step. Page content changes only if an image link had to be rewritten, and each such case is reported.
6. Immediately after, diff the actual `git mv` operations (`git diff -M --summary`) against the Step 2 mapping, entry by entry: every mapped file was moved, nothing extra moved, nothing was missed. Then check that every image link in every moved page resolves to an existing file. Report any mismatch or broken image link before continuing — do not proceed to Step 4 with an unverified migration.
7. Export the confirmed mapping as `old_url,new_url` CSV — Steps 4, 5, and 6 all reuse it.

**Report: mapping validation result (pass/fail per check), number of pages moved, number of images moved and copied, images left in place and why, broken image links (must be 0), number of `index.mdx` created with a table of folder, title, description and character count (all descriptions between 120 and 155), and the result of the comparison against the mapping (missing, extra, mismatched).**

## Step 4 — Fix internal links

Goal: fix every broken internal documentation link caused by the move, repo-wide.

**Source of truth**
- Build the mapping from `git diff -M` (Step 3), not by guessing. Don't invent a mapping for a link to a page that was deleted with no successor — flag those for manual review instead.
- Normalize it: **every internal doc link ends with a `/`**, as the writing guidelines require (relative link with `/` at the start and at the end), including links that had none before. Rewrite `/iam/how-to/manage-members` as `/iam/principals/manage-members/`. Preserve `#anchors` and `?query` strings exactly, with the slash before them: `/path/page#users` becomes `/new/path/page/#users`, and `/path/page?tab=log-in-with-sso-0` becomes `/new/path/page/?tab=log-in-with-sso-0`. This applies to every doc link the skill rewrites or writes, in any file. Redirects (Step 6) follow the opposite convention (no trailing slash): do not mix the two.

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

**Acceptance criteria**: 0 old links left anywhere in scope; every rewritten link resolves to a page that exists; no guardrail case touched; the old → new CSV mapping is up to date with what was actually applied. Every rewritten or written internal doc link ends with a `/` (final check: grep the changed files for internal doc links, outside console URLs, API paths and macro imports, that do not end with `/` before any `#` or `?`; the result must be 0).

**Report: mapping size, files changed by directory, total replacements, unmatched tokens reviewed, dry-run recheck and final grep counts (both must be 0), and links flagged for deleted pages.**

## Step 5 — Update navigation (human checkpoint)

⚠️ `menu/` is a protected directory — never edit `menu.ts` / `navigation.ts` automatically. Propose the new menu entries as a diff for the user to review, and apply it only after explicit per-file confirmation.

**Report: menu entries proposed, which files were changed after confirmation, which were declined.**

## Step 6 — Generate the redirects and open the MR in the website repo

The skill does not touch the website repo and does not open a merge request. It produces one text file, `redirects-<project-name>.txt`, whose content the user copies and pastes at the **end** of `apps/website-proxy/redirects/redirects-website-doc` (website repo, GitLab), then commits and opens the MR themselves. The conventions below come from the real file, not from the Confluence page "Adding a redirection to the documentation websites (content/API)", which is wrong on one point (see the format). If the real file and this step disagree, the real file wins.

0. **Ask the user for the inputs**: the Jira ticket and a short subject for the block comment, and the current content of `redirects-website-doc` (pasted or attached). The file is needed for the comparison in sub-step 3; without it, say that the comparison was not done and list that as a check left to the user.
1. **Format**: one nginx `rewrite` line per redirect, built from the validated CSV:

   ```nginx
   rewrite ^/en/docs/<old_path>(/|$) https://$host/en/docs/<new_path>/ permanent;
   ```

   - Paths take the `/en/docs` prefix on both sides.
   - The **old path has no trailing slash**: the `(/|$)` ending matches it with or without one. Strip the trailing slash from the CSV value.
   - The **new path always ends with a `/`**. The Confluence page says neither path must end with a `/`; that is wrong for the new path, which matches the rest of the file and the trailing slash on internal links (Step 4).
   - Anchors are ignored by redirects; do not encode them.
   - Example from the file: `rewrite ^/en/docs/iam/how-to/set-up-identity-federation(/|$) https://$host/en/docs/iam/user-provisioning/set-up-identity-federation/ permanent;`
   - The block starts with a comment line and a blank line, as the other blocks do: `# Redirect <JIRA-TICKET> - <subject>` (example from the file: `# Redirect WDOC-1298 - Account / IAM / Organizations doc restructuration`).
2. **Validate the mapping before writing the file**:
   - No chains: no `new_path` may also be an `old_path` (A → B → C). No loops, no duplicate `old_path` with different destinations.
   - Prefix capture: `(/|$)` matches the path and everything beneath it. This is correct for ordinary pages and wrong when an old path is the parent of a page that stays live. In the phase 1 mapping, `account/concepts`, `iam/concepts` and `organizations-and-projects/concepts` (redirected to `.../concepts/glossary/`) are such cases: a standard rule would redirect `/en/docs/iam/concepts/overview` to the glossary. Write them as exact matches: `rewrite ^/en/docs/iam/concepts/?$ https://$host/en/docs/iam/concepts/glossary/ permanent;`. Check every entry whose old path is a parent of any new path, not only these three.
   - Rules are evaluated in file order and the first match wins, so no old path may be a path-prefix of another old path.
3. **Compare with the current file** (sub-step 0), entry by entry, and sort each mapping entry into one of these groups:
   - already present with the same destination: skip it (the file may already contain part of the work);
   - already present with a different destination: do not overwrite it and do not write a second rule (the first match wins anyway); list it for the user, with both destinations, for a decision. Example from phase 1: the file sends `account/reference-content/products-availability` and `account/products-availability` to `/en/product-availability-by-region/`, not to the page in the mapping;
   - missing: write it.

   Also check the whole file for existing rules whose destination is one of the old paths: they cause a double redirect and must be updated to the new path. List them for the user, do not edit them.
4. **Write the file** with the comment line, a blank line, and only the missing redirect lines, sorted by section, so it can be pasted as is. Send it to the user, with the groups of sub-step 3 summarized next to it.
5. **Give the user the checks the skill cannot do**, as a short list with the file:
   - Paste the lines at the end of the file, not in the middle.
   - MR title: `feat(website-proxy): implement redirects for <subject> <Jira ticket number>` (example: `feat(website-proxy): implement redirects for AI doc merge MTA-7129`), with the label `REDIRECTS`.
   - Test on staging: wait for the "Merged results" pipeline on the MR, open the environment with **View App**, append an old path (for example `/en/docs/iam/how-to/manage-members/`) and check that the replacement page displays. Test at least one ordinary entry, one with a trailing slash, the three `concepts` entries, and that `/en/docs/iam/concepts/overview/` still loads.
   - Merge order: the redirects should go live with, or before, the docs PR, otherwise old URLs return 404 in the gap.
   - These redirects are temporary: note a removal condition in the MR description (for example once the console, support content and marketing pages use the new URLs).

**Report: number of mapping entries, how many were already present, how many differ from the file (with the list), how many were written, entries written as exact matches, chains or double redirects found, and the path of the file produced.**

## Step 7 — List unused images

Images are moved with their pages in Step 3. This step only lists the ones left unused afterwards (for example originals that were copied to several folders). It never deletes, moves or edits an image: the user decides what to remove.

1. Find images (`.webp`) that are no longer referenced anywhere after the move: for each image in the product-level image folders of the restructured sections (and in `assets/` only for files that were used by those sections), search the whole repo for its file name, including `macros/`, `tutorials/`, `changelog/` and `menu/`. An image used by a macro or a page outside the restructured scope is still in use.
2. Write the candidates to `unused-images-<project-name>.txt`, one path per line, and send it to the user.
3. Flag separately any image that is only referenced from a protected directory (`changelog/`, `menu/`, `blocks/`, `assets/`): it is probably still in use.
4. Tell the user the deletion is theirs to do, after review, and that `assets/` is a protected directory the skill does not edit.

**Report: number of images checked, number of candidates listed, number flagged as referenced only from protected directories, and the path of the file produced.**

## Step 8 — Deliverables

- Old → new URL mapping (CSV), kept as the single source of truth for Steps 4, 5, and 6.
- The redirects file (`redirects-<project-name>.txt`), with the planned removal condition of the redirects.
- The list of unused images (`unused-images-<project-name>.txt`), for the user to review.
- Summary of files changed by directory and total replacements.
- Validation report: dry-run recheck, grep recheck, and any manually-handled edge case (deleted section-index pages, `?query` links, extension-less files).

---

## Gaps this skill will NOT catch automatically

- **Final architecture** — always a human decision, validated with the doc team (Step 2).
- **`menu.ts` / `navigation.ts` changes** — protected directory, human-applied (Step 5).
- **Redirect MR** — the skill only produces the redirects file; the user pastes it into the website repo, opens the MR, and the Website team reviews and merges it (Step 6).
- **SEO re-indexation timeline** — owned by SEO stakeholders, monitored after merge, not predicted here.
