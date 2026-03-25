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
          label: 'Manage a Mailbox subscription',
          slug: 'manage-mailbox-subscription',
        },
        {
          label: 'Delete a Mailbox email account',
          slug: 'delete-email-account',
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
      items: [
        {
          label: 'Mailbox capabilities and limits',
          slug: 'mailbox-capabilities-and-limits',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
  ],
  label: 'Mailbox',
  slug: 'mailbox',
}
