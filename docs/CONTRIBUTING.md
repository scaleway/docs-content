---
permalink: /CONTRIBUTING.md
title: Contributing
---

# Contribute to the Documentation Content

## Who can contribute?

Anyone who has a GitHub account can contribute to the documentation content:

- Users within the Scaleway organization can [open pull requests directly in the docs-content repository](#contribution-procedure-for-internal-scaleway-users).

- External users (i.e. not part of the Scaleway organization) must [fork the repository and open a pull request from the forked repository](#contribution-procedure-for-external-users).

## How to contribute?

### Prerequisites

- You have [Git](https://git-scm.com/) installed
- You have a [GitHub](https://github.com/signup) personal account
- You have installed [yarn](https://yarnpkg.com/getting-started) package manager
- You have [Markdown](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown) and [MDX](https://mdxjs.com/guides/) syntax knowledge
- You have read [the writing guidelines](https://www.scaleway.com/en/docs/guidelines/)

### Contribution procedure for internal Scaleway users

:warning: **Important**
  - All rules below concern this repository.
  - Any PRs which do not comply with the rules below will be rejected.

1. Clone the `docs-content` repository by following the [cloning procedure](#cloning-the-project) below.

2. Make sure you have identified the [type of content](https://github.com/scaleway/docs-content#what-is-the-scaleway-documentation-platform) that you want to write (e.g. tutorial, API/CLI documentation, additional content or troubleshooting).

3. Create your branch locally. All branch names must comply with the following naming convention: `[source]-[action]-[product]`.

    - `source`: Either `int` (for internal Scaleway contributors) or `ext` (for external contributors).

    - `action`: The action you will perform in the documentation you wish to work on, described in 3 letters or less. Example: `add` (for adding content), `rm` (for removing content) or `fix` (for when you wish to fix typos).

    - `product`: the name of the product that corresponds to the documentation page you will edit.

    :information_source: **Example:**
      in the branch `int-add-instances`, an internal contributor will add information to a documentation page of the Instances product category.

4. Make your edits to the documentation. Refer to the [writing guidelines](https://www.scaleway.com/en/docs/guidelines/) to ensure your changes comply with our style guide.

5. Run `git commit -m "type(module): description with some words <BRANCH_NAME>"`. Refer to the [commit naming conventions](#commit-conventions) below to properly name your commit.

6. Run `git push --set-upstream origin <YOUR_BRANCH_NAME>`, and go to [the pull requests page](https://github.com/scaleway/docs-content/pulls) to open a pull request.

    All PR names must comply with the following naming convention: `docs($PRODUCTNAME): $FIXEXPLANATION BRANCHNAME`.


:warning: **Important**
  All PRs are reviewed and approved by the Scaleway Product Documentation team before being merged by them.

---

### Contribution procedure for external users

:warning: **Important**
  - All rules below concern this repository.
  - Any PRs which do not comply with the rules below will be rejected.

1. Access the [docs-content repository](https://github.com/scaleway/docs-content/), and click **Fork** in the top right corner. A form appears.

2. Keep the default values in the form, and click **Create Fork**.

3. Make sure you have identified the [type of content](https://github.com/scaleway/docs-content#what-is-the-scaleway-documentation-platform) that you want to write (e.g. tutorial, API/CLI documentation, additional content or troubleshooting).

4. Create your branch locally. All branch names must comply with the following naming convention: `[source]-[action]-[product]`.

    - `source`: Either `int` (for internal Scaleway contributors) or `ext` (for external contributors). If you are not a Scaleway staff member, use `ext`.

    - `action`: The action you will perform in the documentation you wish to work on, described in 3 letters or less. Example: `add` (for adding content), `rm` (for removing content) or `fix` (for when you wish to fix typos).

    - `product`: the name of the product that corresponds to the documentation page you will edit.

    :information_source: **Example:**
      in the branch `ext-add-instances`, an external contributor will add information to a documentation page of the Instances product category.

4. Make your edits to the documentation. Refer to the [writing guidelines](https://www.scaleway.com/en/docs/guidelines/) to ensure your changes comply with our guidelines.

5. Run `git commit -m "type(module): description of what you performed <BRANCH_NAME>"`. Refer to the [commit naming conventions](#commit-conventions) below to properly name your commit.

6. Run `git push --set-upstream origin <YOUR_BRANCH_NAME>`, and go to the pull request page of the **forked** repository to open a pull request.

7. Click **Create pull request**, then select

  - base repository: `scaleway/docs-content`

  - base: `main`

  - head repository: `<your-account>/docs-content`

  - compare: `<your-branch-with-changes>`

8. Click **Create pull request**.

    All pull requests names must comply with the following naming convention: `docs(<PRODUCT_NAME>): <ACTION> <EXPLANATION> <BRANCH_NAME>`.

:warning: **Important**
  All pull requests are reviewed and approved by the Scaleway Product Documentation team before being merged by them.

---

## Use the repository locally

You have to clone the project locally to work on it.

:warning:
  If you are not a member of the Scaleway organization, you need to fork the repository. [Follow this link](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to find out how.

### Cloning the project

1. Copy the following code and enter it in your terminal:

```bash
git clone git@github.com:scaleway/docs-content.git | bash -s -- cd docs-content && yarn
```

2. Ensure `yarn` has been run, if not run `yarn install`.

## Git commit

Helpful pre-commit commands:

- `pnpm check-slugs` Output slugs that are not kebab-case well formatted.

### Commit conventions

This project uses [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) based on the [Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

Here is a commit template example:

`type(module): description with some words PROJECT-XXX`

Lowercase only, `(module)` is optional. Adding the project number at the end is recommended.

Here is the list of `type` to use (commons in bold):

- `docs`
  - _Do not use other than **project docs** itself concerns (like README file)_
- `feat`
  - _Add new materials (page, sections, …)_
- `fix`
  - _For instance, fix typos, images, …_
- `refactor`
  - _In rare cases, for instance if you have to change folders structures._
- `revert`
  - _Oops case, if you want to redo previous history state_
- `style`
  - _For simple format changes that are not content changes_

### Commit examples

`feat(console): add vpc how-to page MTA-2342`

`fix(iot): wrong image in quickstart`

`style: add bold at scaleway name occurrences MTA-1337`

---

## Markdown

Markdown is a lightweight markup language for creating formatted text using a plain-text editor.

Files with markdown content usually use the `.md` extension.

As we need to use evolved dynamic and designed blocks, for the Scaleway Documentation platform, the choice was to use the extended markdown format, with a special `.mdx` extension.

With MDX files traditional markdown content can be used with React components.

### MDX components

MDX components are useful for adding rich content and interactions within your contributions.

#### Components

This section shows code details listed on a full page.

🔎 [See the full Components page](https://scaleway.com/en/docs/components/).

Feel free to explore this page in your markdown editor to see how the components were used, or in `.mdx` content files that already use MDX components.

### Frontmatter

Any Markdown file that contains a YAML frontmatter block will be processed by Gatsby as a special file.
The front matter must be the first thing in the file and must take the form of a valid YAML set between triple-dashed lines.

Here is a common example used in our `.mdx` files:

```markdown
---
title: How to create a Bare Metal server
description: This page explains how to create a Bare Metal server
tags: compute baremetal bare metal cloud server dedicated
dates:
  validation: 2021-06-22
  posted: 2020-03-12
categories:
  - compute
---

Here starts the content…
```

- `title` and `description`, used for SEO, Algolia & for h1 and description in pages
- `tags` are used to help populate search result lists or pages top. Use space separators.
- `dates` are shown on pages under titles. `validation` must be a date later than the `posted`. Its format should be `AAAA-MM-DD`.

## Writing Guidelines

Refer to the [Scaleway Documentation Guidelines](https://www.scaleway.com/en/docs/guidelines/) for an extensive list of our writing guidelines.
