export const organizationSecurityMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../organization-security',
    },
    {
      label: 'Concepts',
      slug: 'concepts',
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
  ],
  label: 'Organization Security',
  slug: 'organization-security',
}
