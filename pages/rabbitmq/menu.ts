export const rabbitmqMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../rabbitmq',
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
          slug: 'create-rabbitmq-deployment',
        },
        {
          label: 'Connect to a deployment',
          slug: 'connect-to-rabbitmq-deployment',
        },
        {
          label: 'Manage a deployment',
          slug: 'manage-rabbitmq-deployment',
        },
        {
          label: 'Manage the users of a deployment',
          slug: 'manage-users-rabbitmq-deployment',
        },
        {
          label: 'Delete a deployment',
          slug: 'delete-rabbitmq-deployment',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'X y z',
          slug: 'x-y-z',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
  ],
  label: 'Cloud Essentials for RabbitMQ',
  slug: 'rabbitmq',
}
