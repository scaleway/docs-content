export const clustersForKafkaMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../clusters-for-kafka',
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
          label: 'Create a cluster',
          slug: 'create-cluster',
        },
        {
          label: 'Connect to a cluster',
          slug: 'connect-to-cluster',
        },
        {
          label: 'Manage a cluster',
          slug: 'manage-cluster',
        },
        {
          label: 'Delete a cluster',
          slug: 'delete-cluster',
        }
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Clusters for Apache Kafka® API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/clusters-for-kafka/',
        }
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
  ],
  label: 'Clusters for Apache Kafka®',
  slug: 'clusters-for-kafka',
}
