export const annotationsMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../annotations',
    },
    {
      items: [
        {
          label: 'Understanding Annotations',
          slug: 'understanding-annotations',
        },        
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
          label: 'Create and manage annotation keys and values',
          slug: 'create-manage-annotations',
        },        
        {
          label: 'Bind and detach annotations',
          slug: 'bind-and-detach-annotations',
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
          label: 'Scaleway Resource Names',
          slug: 'scaleway-resource-names',
        },
        {
          label: 'Technical rules and limits',
          slug: 'technical-rules-limits',
        },
      ],
      label: 'Reference content',
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
