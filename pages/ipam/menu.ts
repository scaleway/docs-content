export const ipamMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../ipam',
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
          label: 'List your private IP addresses',
          slug: 'list-ips',
        },
        {
          label: 'Manage your private IP addresses',
          slug: 'manage-ips',
        },
        {
          label: 'Reserve an IP address',
          slug: 'reserve-ip',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'IPAM API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/ipam/',
        },
        {
          label: 'Set a reverse IPv6 DNS record',
          slug: 'set-ip-reverse',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Public connectivity: best practices',
          slug: 'public-connectivity-best-practices',
        },
        {
          label: 'IPV6 and the Scaleway ecosystem',
          slug: 'ipv6',
        },
        {
          label: 'Understanding billing for IP addresses',
          slug: 'understanding-ip-billing',
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
  label: 'IPAM',
  slug: 'ipam',
}
