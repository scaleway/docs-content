export default  {
  items: [
    {
      label: 'Overview',
      slug: '../secret-manager',
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
          label: 'Create secrets',
          slug: 'create-secret',
        },
        {
          label: 'Manage a secret',
          slug: 'manage-secret',
        },
        {
          label: 'Filter secrets',
          slug: 'filter-secrets',
        },
        {
          label: 'Add a version',
          slug: 'create-version',
        },
        {
          label: 'Manage a version',
          slug: 'manage-version',
        },
        {
          label: 'Schedule a secret deletion',
          slug: 'delete-secret',
        },
        {
          label: 'Schedule a version deletion',
          slug: 'delete-version',
        },
        {
          label: 'Recover secrets scheduled for deletion',
          slug: 'recover-secrets',
        },
        {
          label: 'Recover a version scheduled for deletion',
          slug: 'recover-version',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: "Secret encryption with Scaleway's Secret Manager",
          slug: 'data-encryption-with-secret-manager',
        },
        {
          label: 'Understanding secret types',
          slug: 'secret-types-json-format',
        },
        {
          label: 'Secret Manager capabilities and limits',
          slug: 'secret-manager-capabilities-limits',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
    {
      items: [
        {
          label: 'Secret Manager API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/secret-manager/',
        },
        {
          label: 'Deploying External Secrets on Kubernetes Kapsule',
          slug: 'external-secrets',
        },
        {
          label: 'Creating a database credentials secret type',
          slug: 'create-secret-with-type',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
  ],
  label: 'Secret Manager',
  slug: 'secret-manager',
}
