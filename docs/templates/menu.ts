export const productnameMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../<>',
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
          label: 'Create a <product-name>',
          slug: 'create-a-<product-name>',
        },
        {
          label: 'Manage the <X> feature',
          slug: 'manage-x',
        },
        {
          label: "Delete a <product-name>",
          slug: "delete-a-<product-name>"
        }
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: '<Product Name> API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/<product-name>/',
        },
        {
          label: 'Creating a <product-name>',
          slug: 'creating-a-<product-name>',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: '<Product Name> features',
          slug: '<product-name>-features',
        },
        {
          label: '<Product Name> limitations',
          slug: '<product-name>-limitations',
        },
        {
          label: 'Information about feature <X>',
          slug: 'info-about-feature-x',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
    {
      label: 'Troubleshooting',
      slug: 'troubleshooting',
    },
  ],
  label: '<Product Name>',
  slug: '<product-name>',
}
