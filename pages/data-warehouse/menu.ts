export const dataWarehouseMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../data-warehouse',
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
          label: 'Create a deployment',
          slug: 'create-deployment',
        },
        {
          label: 'Manage and delete a deployment',
          slug: 'manage-delete-deployment',
        },
        {
          label: 'Connect to a deployment',
          slug: 'connect-applications',
        },
        {
          label: 'Manage databases in a deployment',
          slug: 'manage-databases',
        },
        {
          label: 'Manage users in a deployment',
          slug: 'manage-users',
        },
        {
          label: 'Connect a deployment with BI tools',
          slug: 'connect-bi-tools',
        },
        {
          label: 'Use Private Networks',
          slug: 'use-private-networks',
        },
        {
          label: 'Import data into a deployment',
          slug: 'import-data',
        },
        {
          label: 'Edit the autoscaling of a deployment',
          slug: 'edit-autoscaling',
        },
        {
          label: 'Manage the storage policy of a deployment',
          slug: 'manage-storage',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Example datasets',
          slug: 'example-datasets',
        },
        {
          label: 'Features and limitations',
          slug: 'features-limitations',
        },
      ],
      label: 'Additional content',
      slug: 'reference-content',
    },
  ],
  label: 'Data Warehouse for ClickHouse®',
  slug: 'data-warehouse',
}
