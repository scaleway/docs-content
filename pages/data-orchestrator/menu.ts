export const dataOrchestratorMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../data-orchestrator',
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
          label: 'Create a workflow',
          slug: 'create-workflow',
        },
        {
          label: 'Run a workflow',
          slug: 'run-workflow',
        },
        {
          label: 'Monitor a workflow',
          slug: 'monitor-workflow',
        },
        {
          label: 'Schedule a workflow',
          slug: 'schedule-workflow',
        },
        {
          label: 'Delete a workflow',
          slug: 'delete-workflow',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Logic tasks',
          slug: 'logic-tasks',
        },
        {
          label: 'Cron schedules',
          slug: 'cron-schedules',
        },
      ],
      label: 'Additional content',
      slug: 'reference-content',
    },
  ],
  label: 'Data Orchestrator',
  slug: 'data-orchestrator',
}
