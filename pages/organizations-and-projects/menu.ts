export const organizationsAndProjectsMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../organizations-and-projects',
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
          label: 'Manage Organization quotas',
          slug: 'manage-quotas',
        },
        {
          label: "Set an Organization alias",
          slug: "set-organization-alias"
        },
        {
          label: 'Create a Project',
          slug: 'create-a-project',
        },
        {
          label: 'Change a Project name',
          slug: 'change-project-name',
        },
        {
          label: 'Generate an SSH key',
          slug: 'create-ssh-key',
        },
        {
          label: 'Enforce multifactor authentication',
          slug: 'enforce-mfa',
        },
        {
          label: 'Add resources to a Project',
          slug: 'add-resources-project',
        },
        {
          label: 'Delete a Project',
          slug: 'delete-a-project',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Understanding Organization quotas',
          slug: 'organization-quotas',
        },
      ],
      label: 'Additional Content',
      slug: 'additional-content',
    },
    {
      items: [
        {
          label: 'Managing Projects using Scaleway APIs',
          slug: 'managing-projects',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
  ],
  label: 'Organizations and Projects',
  slug: 'organizations-and-projects',
}
