export const blockStorageMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../block-storage',
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
          label: 'Create a volume',
          slug: 'create-a-volume',
        },
        {
          label: 'Attach a volume',
          slug: 'attach-a-volume',
        },
        {
          label: 'Increase the volume size',
          slug: 'increase-block-volume',
        },
        {
          label: 'Create a snapshot of a Block Storage volume',
          slug: 'create-a-snapshot',
        },
        {
          label: 'Create a Block Storage volume from a snapshot',
          slug: 'create-volume-from-snapshot',
        },
        {
          label: 'Identify the type of a volume or a snapshot',
          slug: 'identify-volumes-snapshot-type',
        },
        {
          label: 'Detach a volume',
          slug: 'detach-a-volume',
        },
        {
          label: 'Unmount a volume',
          slug: 'unmount-a-volume'
        },
        {
          label: 'Delete a snapshot',
          slug: 'delete-a-snapshot',
        },
        {
          label: 'Delete a volume',
          slug: 'delete-a-volume',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Block Storage API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/block-storage/',
        },
        {
          label: 'Managing a volume',
          slug: 'managing-a-volume',
        },
        {
          label: 'Increasing volume size via the API',
          slug: 'increasing-volume-size',
        },
        {
          label: 'Unmounting a volume',
          slug: 'unmounting-a-volume',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label:
            'Differences between Block Storage volumes and Block Storage Low Latency volumes',
          slug: 'differences-between-5kiops-volumes',
        },
        {
          label: 'Block Storage and Instances bandwidth overview',
          slug: 'block-instances-bandwidth-overview',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
  ],
  label: 'Block Storage',
  slug: 'block-storage',
}
