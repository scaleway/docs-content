export const OrganizationSecurityMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../iam',
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
          label: 'Log in as a Member',
          slug: 'log-in-as-a-member',
        },
        {
          label: 'Comply with security requirements as a Member',
          slug: 'comply-with-sec-requirements-member',
        },
        {
          label: 'Enforce security requirements for Members',
          slug: 'enforce-security-requirements-members',
        },
                {
          label: "Set an Organization alias",
          slug: "set-organization-alias"
        },
        {
          label: 'How to set up identity federation',
          slug: 'set-up-identity-federation'
        },
        {
          label: 'How to set up SSO with Authentik',
          slug: 'set-up-sso-with-authentik'
        },
                {
          label: 'Enforce multifactor authentication',
          slug: 'enforce-mfa',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
 
    {
      items: [
        {
          label: 'IAM API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/iam/',
        },
        {
          label: 'Using IAM API keys with Object Storage',
          slug: 'using-api-key-object-storage',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      label: 'Troubleshooting',
      slug: 'troubleshooting',
    },
  ],
  label: 'Organization Security',
  slug: 'organization-security',
}
