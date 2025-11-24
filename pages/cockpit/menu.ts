export const cockpitMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../cockpit',
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
          label: 'Retrieve your Grafana credentials',
          slug: 'retrieve-grafana-credentials',
        },
        {
          label: 'Access Grafana and preconfigured dashboards',
          slug: 'access-grafana-and-managed-dashboards',
        },
        {
          label: 'Use IAM authentication for Cockpit Grafana with Terraform/OpenTofu',
          slug: 'iam-auth-cockpit-grafana-terraform',
        },
        {
          label: 'Create a Cockpit token',
          slug: 'create-token',
        },
        {
          label: 'Create a custom data source',
          slug: 'create-external-data-sources',
        },
        {
          label: 'Delete a custom data source',
          slug: 'delete-external-data-sources',
        },
        {
          label: 'Change data sources retention period',
          slug: 'change-data-retention',
        },
        {
          label: 'Send metrics to Cockpit using Grafana Alloy',
          slug: 'send-metrics-with-grafana-alloy',
        },
        {
          label: 'Send logs from your Kubernetes cluster to Cockpit',
          slug: 'send-logs-from-k8s-to-cockpit',
        },
        {
          label: 'Send metrics from your Kubernetes cluster to Cockpit',
          slug: 'send-metrics-from-k8s-to-cockpit',
        },
        {
          label: 'Create and push and traces to your Cockpit',
          slug: 'activate-push-traces',
        },
        {
          label: 'Configure the alert manager',
          slug: 'enable-alert-manager',
        },
        {
          label: 'Activate Scaleway preconfigured alerts',
          slug: 'activate-managed-alerts',
        },
        {
          label: 'Configure alerts for Scaleway resources',
          slug: 'configure-alerts-for-scw-resources',
<<<<<<< HEAD
        }
=======
        },
        {
          label: 'Retrieve your Grafana credentials',
          slug: 'retrieve-grafana-credentials',
        },
        {
          label: 'Create a token',
          slug: 'create-token',
        },
        {
          label: 'Create and push traces',
          slug: 'activate-push-traces',
        },
        {
          label: 'Access Grafana and preconfigured dashboards',
          slug: 'access-grafana-and-managed-dashboards',
        },
        {
          label: 'Create a custom data source',
          slug: 'create-external-data-sources',
        },
        {
          label: 'Manage data exports',
          slug: 'manage-data-exports',
        },
        {
          label: 'Change data retention period',
          slug: 'change-data-retention',
        },
        {
          label: 'Send metrics to Cockpit using Grafana Alloy',
          slug: 'send-metrics-with-grafana-alloy',
        },
        {
          label:
            'Send metrics from your Kubernetes cluster to Cockpit',
          slug: 'send-metrics-from-k8s-to-cockpit',
        },
        {
          label: 'Send logs from your Kubernetes cluster to Cockpit',
          slug: 'send-logs-from-k8s-to-cockpit',
        },
        {
          label: 'Send metrics and logs to your Cockpit',
          slug: 'send-metrics-logs-to-cockpit',
        },
        {
          label: 'Federate Scaleway metrics with your own Prometheus',
          slug: 'federate-scaleway-metrics',
        },
        {
          label: 'Delete a custom data source',
          slug: 'delete-external-data-sources',
        },
>>>>>>> 5605c9cdb (docs(add): add data export docs)
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Cockpit API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/cockpit/regional-api/',
        },
        {
          label: 'Retrieving logs programmatically using LogCLI',
          slug: 'querying-logs-with-logcli',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label:
            'Understanding and managing Cockpit ingestion to reduce costs',
          slug: 'understanding-cockpit-usage',
        },
        {
          label: 'Cockpit capabilities and limits',
          slug: 'cockpit-limitations',
        },
        {
          label: 'Cockpit pricing information',
          slug: 'cockpit-pricing',
        },
        {
          label:
            'Cockpit supported API endpoints for data source management',
          slug: 'cockpit-supported-endpoints',
        },
        {
          label:
            'Cockpit product integration',
          slug: 'cockpit-product-integration',
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
  label: 'Cockpit',
  slug: 'cockpit',
}
