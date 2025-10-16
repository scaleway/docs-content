export const managedMongodbDatabasesMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../managed-mongodb-databases',
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
          label: 'Create a Database Instance',
          slug: 'create-a-database-instance',
        },
        {
          label: 'Connect a Database Instance to a Private Network',
          slug: 'connect-database-private-network',
        },
        {
          label: 'Connect to a Database Instance',
          slug: 'connect-database-instance',
        },
        {
          label: 'Manage users',
          slug: 'manage-users',
        },
        {
          label: 'Manage snapshots',
          slug: 'manage-snapshots',
        },
        {
          label: 'Increase the storage size',
          slug: 'increase-volume',
        },
        {
          label: 'Delete a Database Instance',
          slug: 'delete-a-database-instance',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Migrating to Managed MongoDB®',
          slug: 'migrating-to-managed-mongodb',
        },
      ],
      label: 'Additional Content',
      slug: 'additional-content',
    },
    {
      items: [
        {
          label: 'Managing users',
          slug: "managing-users-api"
        },
        {
          label: 'Back up and restore MongoDB® Databases',
          slug: 'backup-and-restore',
        },
        {
          label: 'Migrating data with mongosync',
          slug: 'cluster-to-cluster-sync',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
  ],
  label: 'Managed MongoDB®',
  slug: 'managed-mongodb-databases',
}
