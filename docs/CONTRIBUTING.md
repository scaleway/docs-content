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

- **No titles should be orphaned**. For example, if started with H2, you should go down in sequence. So the next step should either be another H2 or a level lower (in this case, H3). 
---

See also: [Anchors and titles components](/components#h2-title)

## Typographical Conventions

### Spelling

At Scaleway we use US English. 

### Capitalization

What should be capitalized: 

- Product and feature names 

### Emboldening

Bold text is used to represent where a user should click or highlight other text relevant to the UI. 

Example:

**Click +Create an Instance to proceed.**

## Code Snippets

Use a code block for examples of:

- commands
- scripts
- outputs

Use inline code snippets when you need to reference information in your text, such as:

- environment variables
- e-mail addresses
- referencing parts of the code block in the text

### Message boxes

**Tip**:	An alternative way of doing the step, or links to additional information about the step.
**Note**:	Information about the consequence(s) of a step.
**Important**: Warning about a possible unwanted consequence (eg delete all data) or possible mistake that could be made during this step.
**Requirements**:	A list of what the user must have already prepared before starting the step-by-step.

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

## Technical Guidelines

### Indentation

Indent new lines within a numbered step, as such:

```md
1. Click **Instances** in the **Compute** section of the side menu. The Instance creation page displays.
 
   <Lightbox src="scaleway-instance-creation-page.png" alt="" />
    
   <Message type="note">
     If you have existing Instances in your account, you will see a list of
     these instances instead of the Instance creation page, and a green **+**
     button for creating new Instances.
   </Message>
2. Enter [...]
```

### Unordered Lists

When including an unordered list within a numbered list, indent each bullet with 4 spaces or 2 tabs.

Example:

```md
3. Complete the following steps in the wizard
    - Choose an **Availability Zone**, which is the geographical region where your instance will be deployed
    - Choose an **Image** to run on your instance. This can be an operating system, an InstantApp or a custom image.
    - Choose an **Instance type**. Different instance types have different prices, processing power, memory, SSD disks and bandwidth.
    - Add **Volumes**. This is an optional step. You can leave the default settings for storage, or choose to add more [block](link) or [local](link) storage to your instance.
    - Enter a **Name** for your instance, or leave the randomly-generated name in place. Optionally, you can also add tags to help you organize your instances.
    - Click **Advanced Options** if you wish to configure a Flexible IP, a local bootscript or a cloud-init configuration.
    - Verify the **SSH Keys** that will be give you access to your Instance
    - Verify the **Estimated Cost** of your instance, based on the specifications you chose.
 
4. Click **Create a new instance** to finish. The creation of your instance is started, and you are informed when the instance is ready.
```
