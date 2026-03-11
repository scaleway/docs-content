export const mailboxMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../mailbox',
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
          label: 'Create your Mailbox domain',
          slug: 'create-mailbox-domain',
        },
        {
          label: 'Configure your Mailbox domain',
          slug: 'configure-mailbox',
        },
        {
          label: 'Delete your Mailbox domain',
          slug: 'delete-mailbox-domain',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Mailbox capabilities and limits',
          slug: 'mailbox-capabilities-and-limits',
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
  label: 'Mailbox',
  slug: 'mailbox',
}
