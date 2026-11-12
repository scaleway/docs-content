export const annotationsMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../annotations',
    },
    {
      items: [
        {
          label: 'Glossary',
          slug: 'glossary',
        },
      ],
      label: 'Concepts',
      slug: 'concepts',
    },    
    {
      label: 'Quickstart',
      slug: 'quickstart',
    },
    {
      items: [
        {
          label: 'Configure Annotations permission sets',
          slug: 'configure-annotations-permissions',
        },
        {
          label: 'Create annotations',
          slug: 'create-annotations',
        },
        {
          label: 'Bind and detach annotations',
          slug: 'bind-and-detach-annotations',
        },
        {
          label: 'Manage keys and values',
          slug: 'manage-keys-values',
        },
      ],
      label: 'Setup and lifecycle',
      slug: 'setup-lifecycle',
    },
    {
      items: [
        {
          label: 'Annotations API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/annotations/',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Scaleway Resource Name',
          slug: 'scaleway-resource-name',
        },
        {
          label: 'Technical rules and limits',
          slug: 'technical-rules-limits',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
    {
      label: 'FAQ',
      slug: 'faq',
    },    
  ],
  label: 'Annotations',
  slug: 'annotations',
}
