---
permalink: /CONTRIBUTING.md
title: Contributing
---

# Contribute with the Documentation Content

## Who can contribute?

Anyone who has a GitHub account can contribute to the documentation content.

## How to contribute?

All rules below concern this repository.
Any PRs which do not comply with the rules below will be rejected.

1. Read and follow [the writing guidelines](#writing-guidelines).
2. Make sure you have identified the [type of content](/scaleway/docs-content#what-is-the-scaleway-documentation-platform) that you want to write (eg: is it a how to, a reference content, a tutorial?).
3. All branch names must comply with the following naming convention: `[source]-[action]-[product]`.
    - `source`: Either `int` (for internal contributor) or `ext` (for external contributor) to Scaleway. If you are not a Scaleway staff member, please use `ext`.
    - `action`: The action you will perform in the documentation you wish to work on, described in 3 letters or less. Example: `add` (for adding content), `rm` (for removing content) or `fix` (for when you wish to fix typos).
    - `product`: the name of the product that corresponds to the documentation page you will edit. 

      So in the branch `ext-add-instances`, an external contributor will add information to a documentation page of the Instances product category.

4. All commit names must comply with the following naming convention: `docs($PRODUCTNAME): $FIXEXPLANATION`.
5. All PR names must comply with the following naming convention: `docs($PRODUCTNAME): $FIXEXPLANATION BRANCHNAME`.
6. All PRs must be reviewed by at least one Technical Writer from the Product Documentation team.
7. All PRs must be approved by at least two Technical Writers from the Product Documentation team before merging to main.

---

## Commit conventions

This project use [conventionalcommits](https://www.conventionalcommits.org/en/v1.0.0/) based on [Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

Here is a commit template exemple:

`type(module): description with some words PROJECT-XXX`

Lowercase only, `(module)` is optional. Project number at the end is recommended.

Here is the list of `type` to use (commons in bold)

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

### examples

`feat(console): add vpc how-to page MTA-2342`

`fix(iot): wrong image in quickstart`

`style: add bold at scaleway name occurences MTA-1337`

---

## Markdown

Markdown is a lightweight markup language for creating formatted text using a plain-text editor.

Files with markdown content usually use the `.md` extension.

As we need to use evolved dynamic and designed blocks, at the Scaleway Documentation platform, the choice was to use the extended markdown format, with a special `.mdx` extension.

With MDX files traditional markdown content can be used with React components.

### MDX components

MDX components are useful to set rich content and interactions within your contributions.

#### Components 

This section shows code details listed in a full page.

🔎 [See the full Components page](https://scaleway-docs.s3-website.fr-par.scw.cloud/components/).

Feel free to explore this page in your markdown editor to see how the components were used, or in `.mdx` content files that already use MDX components.

### Frontmatter

Any Markdown file that contains a YAML frontmatter block will be processed by Gatsby as a special file.  
The front matter must be the first thing in the file and must take the form of a valid YAML set between triple-dashed lines.

Here is a common example used in our `.mdx` files:

```markdown
---
title: How to create a Bare Metal server
description: This page explains how to create a Bare Metal server
image: /images/scaleway-account.png
tags: compute baremetal bare metal cloud server dedicated
dates:
  validation: 2021-06-22
  posted: 2020-03-12
steps:
  - step: Configuring the CLI
    url: https://www.scaleway.com/en/docs/compute/bare-metal-cloud/api-cli/bare-metal-with-cli/#-Configuring-the-CLI
  - step: Creating a Bare Metal Server
    url: https://www.scaleway.com/en/docs/compute/bare-metal-cloud/api-cli/bare-metal-with-cli/#-Creating-a-Bare-Metal-Server
  - step: Installing an OS
    url: https://www.scaleway.com/en/docs/compute/bare-metal-cloud/api-cli/bare-metal-with-cli/#-Installing-an-OS/
  - step: Using Other CLI Commands
    url: https://www.scaleway.com/en/docs/compute/bare-metal-cloud/api-cli/bare-metal-with-cli/#-Using-Other-CLI-Commands
---

Here starts the content…
```

- `title` is used as H1 in pages, in the html head element as the browser tab title and for SEO.
- `description` is used in pages and in the head element for SEO.
- `image` is used for Hero section image in tutorials pages. Path could be relative to file.
- `tags` are used to help populate search result lists or pages top.
- `dates` are showed in pages under titles. `validation` must be a date later than the `posted`. Format should be `AAAA-MM-DD`
- `steps` are used in JSON+LD script tag in html head. It respects the schema.org format and is used for SEO, as Google could show steps in search results. 

---

## Writing Guidelines

