export const serverlessSqlDatabasesMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../serverless-sql-databases',
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
          label: 'Create a Serverless SQL Database',
          slug: 'create-a-database',
        },
        {
          label: 'Connect to a Serverless SQL Database',
          slug: 'connect-to-a-database',
        },
        {
          label: 'Add users to a Serverless SQL Database',
          slug: 'add-users',
        },
        {
          label:
            'Manage user permissions for Serverless SQL Databases',
          slug: 'manage-permissions',
        },
        {
          label: 'Use Row-Level Security on a database',
          slug: 'use-row-level-security',
        },
        {
          label: "Edit a Serverless SQL Database's autoscaling",
          slug: 'configure-autoscaling',
        },
        {
          label: 'Manage backups for Serverless SQL Databases',
          slug: 'manage-backups',
        },
        {
          label: 'Delete a Serverless SQL Database',
          slug: 'delete-a-database',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Serverless SQL Database API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/serverless-sql-databases/',
        },
        {
          label: 'Importing data into Serverless SQL Databases',
          slug: 'import-data-to-serverless-sql-databases',
        },
        {
          label: 'Securing connections using SSL/TLS',
          slug: 'secure-connection-ssl-tls',
        },
        {
          label: 'Using Row-Level Security with PostgREST',
          slug: 'postgrest-row-level-security',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label:
            'Known differences between Serverless SQL Databases and PostgreSQL',
          slug: 'known-differences',
        },
        {
          label: 'Serverless SQL Databases overview',
          slug: 'serverless-sql-databases-overview',
        },
        {
          label: 'Supported PostgreSQL extensions',
          slug: 'supported-postgresql-extensions',
        },
        {
          label: 'Planned maintenance',
          slug: 'planned-maintenance',
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
  label: 'Serverless SQL',
  slug: 'serverless-sql-databases',
}
