export const annotationsMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../annotations',
    },
    {
      label: 'Concepts',
      slug: 'concepts',
    },
    {
      label: 'Quickstart',
      slug: 'quickstart',
    },
    {
      label: 'FAQ',
      slug: 'faq',
    },
    {
      items: [
        {
          label: 'Configure Annotations permission sets',
          slug: 'configure-annotations-permissions',
        },
        {
          label: 'Use annotations',
          slug: 'how-to-use-annotations',
        },
      ],
      label: 'How to',
      slug: 'how-to',
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
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
  ],
  label: 'Annotations',
  slug: 'annotations',
}
