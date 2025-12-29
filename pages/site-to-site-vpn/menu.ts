export const siteToSiteVpnMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../site-to-site-vpn',
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
          label: 'Create and manage a VPN gateway',
          slug: 'create-manage-vpn-gateway',
        },
        {
          label: 'Create and manage a customer gateway',
          slug: 'create-manage-customer-gateway',
        },
                {
          label: 'Create and manage a routing policy',
          slug: 'create-manage-routing-policy',
        },
        {
          label: 'Create and manage a VPN connection',
          slug: 'create-manage-vpn-connection',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Site-to-Site VPN API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/site-to-site-vpn/',
        }
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Understanding Site-to-Site VPN',
          slug: 'understanding-s2svpn',
        },
        {
          label: 'Site-to-Site VPN Security proposals',
          slug: 'security-proposals',
        },
        {
          label: 'Site-to-Site VPN Statuses',
          slug: 'statuses',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    }
  ],
  label: 'Site-to-Site VPN',
  slug: 'site-to-site-vpn',
}
