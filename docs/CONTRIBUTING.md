---
permalink: /CONTRIBUTING.md
title: Contributing
---

# Contribute to the Documentation Content

## Who can contribute?

Anyone who has a GitHub account can contribute to the documentation content.

## How to contribute?

### Prerequisites

- You have [Git](https://git-scm.com/) installed
- You have a [GitHub](https://github.com/signup) personal account
- You have installed [Yarn](https://yarnpkg.com/getting-started) package manager
- You have [Markdown](https://guides.github.com/features/mastering-markdown/#GitHub-flavored-markdown) and [MDX](https://mdxjs.com/guides/) syntax knowledge
- You have read [the writing guidelines](#writing-guidelines)

:warning: **Important**

  - All rules below concern this repository.
  - Any PRs which do not comply with the rules below will be rejected.

1. Clone the `docs-content` repository by following the [cloning procedure](#cloning-the-project) below.

2. Make sure you have identified the [type of content](https://github.com/scaleway/docs-content#what-is-the-scaleway-documentation-platform) that you want to write (e.g. tutorial, API/CLI documentation, reference content or troubleshooting).

3. Create your branch. All branch names must comply with the following naming convention: `[source]-[action]-[product]`.

    - `source`: Either `int` (for internal Scaleway contributors) or `ext` (for external contributors). If you are not a Scaleway staff member, please use `ext`.

    - `action`: The action you will perform in the documentation you wish to work on, described in 3 letters or less. Example: `add` (for adding content), `rm` (for removing content) or `fix` (for when you wish to fix typos).

    - `product`: the name of the product that corresponds to the documentation page you will edit.

    :information_source: Example:
      in the branch `ext-add-instances`, an external contributor will add information to a documentation page of the Instances product category.

4. Make your edits to the documentation. Refer to the [writing guidelines](#writing-guidelines) below to ensure your changes comply with our style guide.

5. Run `git commit -m "type(module): description with some words <BRANCH_NAME>"`. Refer to the [commit naming conventions](#commit-conventions) below to properly name your commit.

6. Run `git push --set-upstream origin <YOUR_BRANCH_NAME>`, and go to [the pull requests page](https://github.com/scaleway/docs-content/pulls) to open a pull request.

All PR names must comply with the following naming convention: `docs($PRODUCTNAME): $FIXEXPLANATION BRANCHNAME`.

  :warning: **Important**
    All PRs are reviewed and approved by the Scaleway Product Documentation team before being merged by them.
---

## Use repository locally

You have to clone the project locally to work on it.

:warning:
  If you are not a member of the Scaleway organization, you need to fork the repository. [Follow this link](https://docs.github.com/en/get-started/quickstart/fork-a-repo) to find out how.

### Cloning the project

1. Copy the following code and enter it in your terminal:

```bash
git clone git@github.com:docs-content.git | bash -s -- cd docs-content && yarn
```

2. Ensure `yarn` has been run, if not run `yarn install`.

## Git commit

Helpful pre-commit commands:

- `yarn check-slugs` Output slugs that are not kebab-case well formatted.

### Commit conventions

This project uses [conventionalcommits](https://www.conventionalcommits.org/en/v1.0.0/) based on the [Angular convention](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines).

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

### Commit name examples

`feat(console): add vpc how-to page MTA-2342`

`fix(iot): wrong image in quickstart`

`style: add bold at scaleway name occurences MTA-1337`

---

## Markdown

Markdown is a lightweight markup language for creating formatted text using a plain-text editor.

Files with markdown content usually use the `.md` extension.

As we need to use evolved dynamic and designed blocks, for the Scaleway Documentation platform, the choice was to use the extended markdown format, with a special `.mdx` extension.

With MDX files traditional markdown content can be used with React components.

### MDX components

MDX components are useful for adding rich content and interactions within your contributions.

#### Components

This section shows code details listed in a full page.

🔎 [See the full Components page](https://scaleway.com/en/docs/components/).

Feel free to explore this page in your markdown editor to see how the components were used, or in `.mdx` content files that already use MDX components.

### Frontmatter

Any Markdown file that contains a YAML frontmatter block will be processed by Gatsby as a special file.  
The front matter must be the first thing in the file and must take the form of a valid YAML set between triple-dashed lines.

Here is a common example used in our `.mdx` files:

```markdown
---
meta:
  title: How to create a Bare Metal server
  description: This page explains how to create a Bare Metal server
content:
  h1: Bare Metal server
  paragraph: This is a tutorial Bare Metal
hero: assets/scaleway-account.png
tags: compute baremetal bare metal cloud server dedicated
dates:
  validation: 2021-06-22
  posted: 2020-03-12
---

Here starts the content…
```

- `meta` part is used for SEO `title` and `description`, it don't appear inside the website
- `content` part which contain `h1` and `paragraph` is used for title and description inside website pages.
- `h1` is used as H1 in pages, in the html head element as the browser tab title and for SEO.
- `paragraph` is used in pages and in the head element for SEO.
- `image` is used for Hero section image in tutorials pages. Path could be relative to file.
- `tags` are used to help populate search result lists or pages top.
- `dates` are showed in pages under titles. `validation` must be a date later than the `posted`. Format should be `AAAA-MM-DD`

## Writing Guidelines

### Requirements

In this section, point out what the user must have already prepared before starting the step-by-step. Include links to other documentation pages.

Example:

---

**Requirements**

- You have a Scaleway Account
- You have configured your SSH key

---

See also: [Message boxes typographical conventions](#message-boxes)

### Titles/Anchors

You can go up to 5 hierarchy levels (H1, H2, H3, H4, H5).

---

**Important**

- In the right menu, **only H1 and H2 are visible**.

- **No titles should be orphaned**. For example, if you started with H2, you should go down in sequence. So the next step should either be another H2 or a level lower (in this case, H3).

---

See also: [Anchors and titles components](/components#h2-title)

## Typographical Conventions

### Spelling

At Scaleway we use US English.

### Capitalization

What should be capitalized:

- Product names

### Emboldening

Bold text is used to represent where a user should click or highlight other text relevant to the UI.

Example:

Click **+Create an Instance to proceed.**

## Code Snippets

Use a code block for examples of:

- commands
- scripts
- outputs

Use inline code when you need to reference information in your text, such as:

- environment variables
- e-mail addresses
- referencing parts of the code block in the text

### Message boxes

Message boxes help you highlight important or pertinent information.

**Tip**: An alternative way of doing the step, or links to additional information about the step.

**Note**: Information about the consequence(s) of a step.

**Important**: Warning about a possible unwanted consequence (eg delete all data) or possible mistake that could be made during this step.

**Requirements**: A list of what the user must have already prepared before starting the step-by-step.

See also: [Message box components](/components#messages)

### Environment Variables

When referring to API calls or CLI commands, follow the environment variable conventions listed on [this page](https://github.com/scaleway/scaleway-sdk-go/tree/master/scw#environment-variables). Use the same format for other variables.

Example:

```
$EMAIL_ADDRESS
```

If you need to use an example of IP addresses, some IP ranges are reserved for documentation:

**IPv4**

192.0.2.0/24

198.51.100.0/24

203.0.113.0/24

233.252.0.0/24

**IPv6**

2001:db8::/32

## Screenshot Guidelines

### Format

Save screenshots in `.png` format.

### Information to omit

Omit any personal information (such as e-mail addresses, addresses, telephone numbers, the Scaleway resource ID, etc). Use the blur effect over the information you wish to conceal.

### Captions

If the image contents are already being described in the documentation text, there is no need to include a caption. To increase accessibility, if new information is being presented in the image, include a description (`alt="caption"`).

### Image Names

Start with “Scaleway” and make the name as explicit as possible, describing the screenshot.

Example:

`scaleway-top-right-menu.png` or `scaleway-leave-organization`
