---
title: Agents metadata
description: Overview of the docs‑content repository for AI‑agents
---

# AGENTS.md - Scaleway Documentation Content

## Purpose

This file helps AI/LLM agents understand the structure, tooling, and conventions of the
Scaleway documentation repository so they can make consistent, high-quality contributions.

## Project Overview

This repository hosts the **Scaleway Documentation** content. The goal of Scaleway documentation is to provide information about all resources in the Scaleway ecosystem and the procedures users should follow to get the best experience from products and services.

**Repository**: [scaleway/docs-content](https://github.com/scaleway/docs-content)  
**Website**: [scaleway.com/en/docs](https://www.scaleway.com/en/docs/)

Scaleway documentation content is authored in MDX and includes React components to add dynamic, interactive elements.

## Content Types

| PAGE TYPE          | DESCRIPTION                                                                              |
| -------------------| ---------------------------------------------------------------------------------------- |
| How to             | Shows how to do a core action (e.g. create, configure, delete, use features) for a Scaleway product via the console, e.g. [How to create a Load Balancer](/load-balancer/how-to/create-load-balancer/)                                        |
| Quickstart         | Shows how to do the main series of actions necessary to start using a Scaleway product via the console, e.g. [Instances Quickstart](/instances/quickstart/)                                   |
| Concepts           | Defines and briefly explains the main terminology associated with a Scaleway product, e.g. [Kubernetes Concepts](/kubernetes/concepts/)                                            |
| Troubleshooting    | Gives solutions to help resolve a common issue with a Scaleway product, e.g. [VPC auto-config is not working](/vpc/troubleshooting/autoconfig-not-working/). Refer to the [troubleshooting template](https://github.com/scaleway/docs-content/blob/main/docs/TROUBLESHOOTING_TEMPLATE.mdx) for more information       |
| API/CLI          | Presents information and tips for creating and configuring a Scaleway product via both official and third-party APIs, CLIs, SDKs and other developer tools, e.g. Terraform/OpenTofu, e.g. [Using Object Storage with the AWS-CLI](/object-storage/api-cli/object-storage-aws-cli/). These pages complement the [main developer reference documentation](https://www.scaleway.com/en/developers/).                           |
| Additional Content | Provides detailed information on specific subjects and features associated with a Scaleway product, e.g. [Optimize your Object Storage performance](/object-storage/reference-content/optimize-object-storage-performance/)                                            |
| Tutorial           | Explains how to use a Scaleway product with a third-party tool, or how to use multiple Scaleway products together for a specific use-case, e.g. [Deploying Strapi on an Instance](/tutorials/strapi/)                                            |
| FAQ                | Gives answers to the most frequently asked questions about Scaleway products, e.g. [Cockpit FAQ](/cockpit/faq/)                                            |

## Directory Structure

```
docs-content/
├── pages/                          # Main documentation content organized by product
│   ├── instances/                  # Example: Instances product documentation
│   │   ├── index.mdx               # Product landing page
│   │   ├── menu.ts                 # Navigation menu structure
│   │   ├── concepts/               # Concept pages
│   │   ├── quickstart/             # Quickstart guides
│   │   ├── how-to/                 # How-to guides
│   │   ├── reference-content/      # Additional content
│   │   ├── api-cli/                # API/CLI documentation
│   │   └── troubleshooting/        # Troubleshooting guides
│   ├── billing/                    # Billing documentation
│   ├── kubernetes/                 # Kubernetes documentation
│   └── ...                         # 50+ product directories
├── macros/                         # Reusable content components organized by product
│   ├── compute/                    # Compute-related macros
│   ├── storage/                    # Storage-related macros
│   ├── network/                    # Network-related macros
│   └── ...                         # Product-specific macros
├── changelog/                      # Product changelog entries
│   ├── instances/                  # Instances changelogs by date
│   ├── kubernetes/                 # Kubernetes changelogs by date
│   └── ...                         # Product-specific changelogs
├── blocks/                         # Reusable UI blocks (callToAction, feedback, etc.)
├── menu/                           # Global navigation configuration
│   ├── navigation.ts               # Main navigation structure
│   ├── mainLinks.json              # Main navigation links
│   ├── footer.json                 # Footer links
│   └── filters.json                # Content filters
├── assets/                         # Global assets (images, PDFs)
├── docs/                           # Project documentation
│   ├── CONTRIBUTING.md             # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md          # Code of conduct
│   ├── DOC_PAGE_TEMPLATE.mdx       # Page template
│   └── PULL_REQUEST_TEMPLATE.md    # PR template
└── tutorials/                      # Standalone tutorial content
```

## Content Authoring Conventions

### Frontmatter Structure

All `.mdx` pages use YAML frontmatter:

```yaml
---
title: Page Title
description: One-sentence description for SEO
tags: tag1 tag2 tag3
dates:
  validation: 2024-01-01
  posted: 2024-01-01
categories:
  - product-category
---
```

### Navigation Structure

Each product directory contains a `menu.ts` file defining its navigation. The following example uses the Instances product to illustrate how `menu.ts` works.

```typescript
export const instancesMenu = {
  label: 'CPU Instances',
  slug: 'instances',
  items: [
    { label: 'Overview', slug: '../instances' },
    { label: 'Concepts', slug: 'concepts' },
    { label: 'Quickstart', slug: 'quickstart' },
    { label: 'How to', slug: 'how-to', items: [...] },
    { label: 'API/CLI', slug: 'api-cli', items: [...] },
    { label: 'Additional Content', slug: 'reference-content', items: [...] },
    { label: 'Troubleshooting', slug: 'troubleshooting' },
  ],
}
```

### Macros

Macros are reusable content components with their own frontmatter:

```yaml
---
macro: compute-instances
---
```

Macros embed consistent, reusable content snippets across multiple pages from a single source.

### MDX Components

This project uses MDX (Markdown + React components). Key components include:

- `<Message>` - Note, tip, warning, important messages
- `<Grid>` - Grid layout container
- `<SummaryCard>` - Card components for navigation
- `<ProductHeader>` - Product landing page headers
- `<Tabs>` - Tabbed content
- `<CodeBlock>` - Syntax-highlighted code blocks
- `<Table>` - Data tables

For full component reference, see: [storybook-docs.scaleway.com](https://storybook-docs.scaleway.com/)

## Writing Guidelines

See [Writing Guidelines](.pages/guidelines.mdx) for the full documentation style guide.

- Language: Use American English (US English) spelling exclusively (e.g., "center" not "centre", "recognize" not "recognise").
- Tone: Use present tense, active voice. Maintain a formal tone. Do not use passive voice, "please", "thank you", future tense, or contractions.
- Pronouns: Address the user as "you". Refer to Scaleway as "Scaleway".
- File format: All pages must be .mdx files. All images must be .webp format.
- Page structure: Include metadata in the frontmatter YAML, Introduction, Requirements (when applicable), and Page body in that order.
- Headings: Treat the title in the frontmatter YAML as the H1 heading, it must be the only H1 heading, and use H2/H3 for subsections. All headings must be in sentence case.
- Numbered steps: Use numbered steps for instructions. Each step = one action, starting with an imperative verb.
- Code blocks: Use triple backticks with language specification (e.g., ```python).
- Inline code: Use backticks for environment variables, placeholders, and short code snippets.
- Links: Use descriptive link text (not "here" or "this page"). Use relative links with leading and trailing slashes for internal pages.
- Admonitions: Use one of the following message boxes: Tip, Note, Important. Do not use tables in message boxes.
- Bold text: Use bold for console navigation elements and button names (e.g., Click Create Instance).
- Capitalization: Capitalize product names (Instance, Load Balancer). Do not capitalize feature names unless they are Scaleway-specific terms (InstantApp, Easy Deploy). Use sentence-case capitalization in titles and headings.
- Numbers: Write numbers 1-9 in full. Use numerals for 10+. Use commas to separate thousands.
- Dates/Times: Use 24-hour format for times. Use day/month/year or DD/MM/YY for dates. Avoid ordinals (e.g., "14 January" not "14th January").

## Product Categories

The navigation of the documentation website [scaleway.com/en/docs](https://www.scaleway.com/en/docs/) is organized into these main categories (to match the navigation of the Scaleway console):

### Management & Governance

- Account, Billing, Environmental Footprint
- Security & Identity (IAM, Key Manager, Organizations, Secret Manager)

### Products

- **AI**: Generative APIs
- **Bare Metal**: Apple Silicon, Elastic Metal, Dedibox
- **Compute**: Instances, GPU
- **Containers**: Container Registry, Kubernetes
- **Databases**: PostgreSQL/MySQL, Redis, MongoDB, OpenSearch, Serverless SQL
- **Data & Analytics**: Data Orchestrator, Data Warehouse, Apache Spark, Kafka, NATS
- **Developer Tools**: CLI, SDK, Terraform
- **Domains & Web Hosting**: Domains/DNS, Mailbox, TEM, Webhosting
- **Integration Services**: IoT Hub, Topics/Events, Queues, RabbitMQ
- **Monitoring**: Audit Trail, Cockpit
- **Network**: Edge Services, Interlink, IPAM, Load Balancer, Public Gateways, VPN, VPC
- **Serverless**: Containers, Functions, Jobs
- **Storage**: Block Storage, File Storage, Local Storage, Object Storage

### Dedibox (separate console)

- Dedibox Console, Servers, Network

## Contributing

See [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for the full guide.

### Branch Naming Convention

```
[source]-[action]-[product]
```

- `source`: `int` (internal) or `ext` (external)
- `action`: `add`, `rm`, `fix`
- `product`: product name (e.g., `instances`, `kubernetes`)

**Example**: `int-add-instances`, `ext-fix-kubernetes`

### Commit Convention

Based on [Conventional Commits](https://www.conventionalcommits.org/):

```
type(module): description PROJECT-XXX
```

**Types**:
- `docs` - Project documentation (README, CONTRIBUTING, etc.)
- `feat` - New content (pages, sections)
- `fix` - Bug fixes (typos, images, etc.)
- `refactor` - Structural changes
- `revert` - Reverting changes
- `style` - Formatting changes

**Examples**:
- `feat(console): add vpc how-to page MTA-2342`
- `fix(iot): wrong image in quickstart`
- `style: add bold at scaleway name occurrences MTA-1337`

### Pull Request Naming

```
docs(product_name): description with some words
```

### Agent Attributions

All agent-drafted content must add `draftedBy` metadata as the last line of the YAML frontmatter, using the following format:

```yaml
---
title: Page Title
description: One-sentence description for SEO
tags: tag1 tag2 tag3
dates:
  validation: 2024-01-01
  posted: 2024-01-01
categories:
  - product-category
draftedBy: agent-name version
---
```

### Strict Boundaries

- You MAY edit files in the `macros`, `pages`, and `tutorials` directories.
- You MUST NEVER modify files in the `.github`, `assets`, `bin`, `blocks`, `changelog`, `docs`, `menu`, and the root directories.

## Building and Serving Locally

This repository only hosts the documentation site content, and does not include any of the frontend or backend components required to build or render the site.

## Important Notes

- This repository contains **content only** - no frontend/backend for building the site
- Internal Scaleway users have access to internal preview tools
- All PRs are reviewed and approved by the Scaleway Product Documentation team
- Files use `.mdx` extension for extended Markdown with React components
- Slugs must be kebab-case

## Related Resources

- [Writing Guidelines](.pages/guidelines.mdx)
- [MDX Components](https://storybook-docs.scaleway.com/)
- [Contributing Guide](./docs/CONTRIBUTING.md)
- [Code of Conduct](./docs/CODE_OF_CONDUCT.md)