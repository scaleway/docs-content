export const localStorageMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../local-storage',
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
      items: [
        {
          label: 'Create a volume',
          slug: 'create-volume',
        },
        {
          label: 'Attach a volume',
          slug: 'attach-volume',
        },
        {
          label: 'Create a snapshot of a Local Storage volume',
          slug: 'create-snapshot',
        },
        {
          label: 'Create a Local Storage volume from a snapshot',
          slug: 'create-volume-from-snapshot',
        },
        {
          label: 'Detach a volume',
          slug: 'detach-volume',
        },
        {
          label: 'Delete a snapshot',
          slug: 'delete-snapshot',
        },
        {
          label: 'Delete a volume',
          slug: 'delete-volume',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
  ],
  label: 'Local Storage',
  slug: 'local-storage',
}
