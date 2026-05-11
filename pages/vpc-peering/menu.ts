export const vpcPeeringMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../vpc-peering',
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
          label: 'VPC Peering API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/vpc/',
        }
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Create a peering connector',
          slug: 'create-peering-connector',
        },
        {
          label: 'Manage a peering connector',
          slug: 'manage-peering-connector',
        },
        {
          label: 'Delete a peering connector',
          slug: 'delete-peering-connector',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Understanding VPC Peering',
          slug: 'understanding-vpc-peering',
        },
        {
          label: 'Features and limitations',
          slug: 'features-limitations',
        },
        {
          label: 'VPC Peering statuses',
          slug: 'statuses',
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
  label: 'VPC Peering',
  slug: 'vpc-peering',
}