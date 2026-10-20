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
          label: 'List your IP addresses',
          slug: 'list-ips',
        },
        {
          label: 'Manage your IP addresses',
          slug: 'manage-ips',
        },
        {
          label: 'Reserve an IP address',
          slug: 'reserve-ip',
        },
        {
          label: 'Attach a resource using a reserved IP',
          slug: 'attach-resource',
        },
        {
          label: 'Release a reserved IP address',
          slug: 'release-ip',
        },
        {
          label: 'Manage reverse DNS',
          slug: 'set-ip-reverse',
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
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Understanding IPAM',
          slug: 'understanding-ipam',
        },
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
