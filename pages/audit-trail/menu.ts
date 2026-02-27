export const auditTrailMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../audit-trail',
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
          label: 'Configure the Audit Trail permission set',
          slug: 'configure-audit-trail-permissions',
        },
        {
          label: 'Use Audit Trail',
          slug: 'use-audit-trail',
        },
        {
          label: 'Create and manage Audit Trail exports',
          slug: 'manage-adt-export',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Audit Trail API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/audit-trail/',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Audit Trail product integration',
          slug: 'resource-integration-with-adt',
        },
        {
          label: 'IAM authentication events in Audit Trail',
          slug: 'iam-authentication-events',
        },
        {
          label: 'Supported endpoints for Audit Trail',
          slug: 'adt-supported-endpoints',
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
  label: 'Audit Trail',
  slug: 'audit-trail',
}
