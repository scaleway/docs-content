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
          label: 'Reset a Mailbox email account password',
          slug: 'reset-mailbox-password',
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
    }
  ],
  label: 'Mailbox',
  slug: 'mailbox',
}
