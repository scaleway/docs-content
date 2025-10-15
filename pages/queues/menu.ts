export const queuesMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../queues',
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
          label: 'Create credentials',
          slug: 'create-credentials',
        },
        {
          label: 'Manage credentials',
          slug: 'manage-credentials',
        },
        {
          label: 'Create and manage queues',
          slug: 'create-manage-queues',
        },
        {
          label: 'Monitor Queues with Cockpit',
          slug: 'monitor-queues-cockpit',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Queues API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/queues/sqs-api/',
        },
        {
          label: 'Connecting Queues to the AWS-CLI',
          slug: 'connect-aws-cli',
        },
        {
          label: 'Using Queues with the AWS-CLI',
          slug: 'queues-aws-cli',
        },
        {
          label: 'Using Go, Python or Node.js with Queues',
          slug: 'python-node-queues',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Queues overview',
          slug: 'queues-overview',
        },
        {
          label: 'Queues - supported actions',
          slug: 'queues-support',
        },
        {
          label: 'Limitations',
          slug: 'limitations',
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
  label: 'Queues',
  slug: 'queues',
}
