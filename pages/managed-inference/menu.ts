export const managedInferenceMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../managed-inference',
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
          label: 'Deploy a model',
          slug: 'create-deployment',
        },
        {
          label: 'Import a custom model',
          slug: 'import-custom-model',
        },
        {
          label: 'Change the model of a deployment',
          slug: 'change-model',
        },
        {
          label: 'Monitor a deployment',
          slug: 'monitor-deployment',
        },
        {
          label: 'Configure autoscaling',
          slug: 'configure-autoscaling',
        },
        {
          label: 'Manage access to a deployment',
          slug: 'manage-allowed-ips',
        },
        {
          label:
            'Use your Managed Inference deployment with a Private Network',
          slug: 'managed-inference-with-private-network',
        },
        {
          label: 'Delete a deployment',
          slug: 'delete-deployment',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Managed Inference API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/managed-inference/',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label:
            "Data, privacy, and security for Scaleway's AI services",
          slug: 'data-privacy-security-scaleway-ai-services',
        },
        {
          label: 'OpenAI API compatibility',
          slug: 'openai-compatibility',
        },
        {
          label: 'Supported models in Managed Inference',
          slug: 'supported-models',
        },
        {
          label:
            'Support for function calling in Scaleway Managed Inference',
          slug: 'function-calling-support',
        },
        {
          label: 'Managed Inference model catalog',
          slug: 'model-catalog',
        },
      ],
      label: 'Additional Content',
      slug: 'reference-content',
    },
  ],
  label: 'Managed Inference',
  slug: 'managed-inference',
}
