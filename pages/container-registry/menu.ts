export const containerRegistryMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../container-registry',
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
          label: 'Create a namespace',
          slug: 'create-namespace',
        },
        {
          label: 'Connect the Docker CLI',
          slug: 'connect-docker-cli',
        },
        {
          label: 'Push images',
          slug: 'push-images',
        },
        {
          label: 'Pull images',
          slug: 'pull-images',
        },
        {
          label: 'Display image versions',
          slug: 'display-image-versions',
        },
        {
          label: 'Manage image privacy settings',
          slug: 'manage-image-privacy-settings',
        },
        {
          label: 'Manage namespace privacy policies',
          slug: 'manage-namespace-privacy-policies',
        },
        {
          label: 'Delete an image',
          slug: 'delete-image',
        },
        {
          label: 'Delete a namespace',
          slug: 'delete-namespace',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Container Registry API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/registry/',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      label: 'Troubleshooting',
      slug: 'troubleshooting',
    },
  ],
  label: 'Container Registry',
  slug: 'container-registry',
}
