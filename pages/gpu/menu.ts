export const gpuMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../gpu',
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
          label: 'Create and manage a GPU Instance',
          slug: 'create-manage-gpu-instance',
        },
        {
          label: 'Use Docker on your GPU Instance',
          slug: 'use-gpu-with-docker',
        },
        {
          label: 'Use NVIDIA MIG technology on GPU Instances',
          slug: 'use-nvidia-mig-technology',
        },
        {
          label: 'Use NVIDIA MIG technology with Kubernetes',
          slug: 'use-mig-with-kubernetes',
        },
        {
          label: 'Use the scratch storage on H100 GPU Instances',
          slug: 'use-scratch-storage-h100-instances',
        },
        {
          label: 'Use the preinstalled environment',
          slug: 'use-preinstalled-env',
        },
        {
          label: 'Use pipenv to create virtual environments',
          slug: 'use-pipenv',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Instances API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/instances/',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Choosing the right GPU Instance type',
          slug: 'choosing-gpu-instance-type',
        },
        {
          label:
            'GPU Instances internet and Block Storage bandwidth overview',
          slug: 'gpu-instances-bandwidth-overview',
        },
        {
          label: 'Migrating from H100-2-80G to H100-SXM-2-80G',
          slug: 'migration-h100',
        },
        {
          label: 'GPU time-slicing with Kubernetes',
          slug: 'kubernetes-gpu-time-slicing',
        },
        {
          label: 'Docker AI images',
          slug: 'docker-images',
        },
        {
          label: 'Understanding NVIDIA GPU Cloud (NGC)',
          slug: 'understanding-nvidia-ngc',
        },
        {
          label: 'Understanding NVIDIA NeMo (Neural Models)',
          slug: 'understanding-nvidia-nemo',
        },
        {
          label: 'Understanding the NVIDIA TAO toolkit',
          slug: 'understanding-nvidia-tao',
        },
        {
          label: 'Understanding NVIDIA FP4 format',
          slug: 'understanding-nvidia-fp4',
        },
        {
          label: 'Understanding NVIDIA FP8 format',
          slug: 'understanding-nvidia-fp8',
        },
        {
          label: 'Understanding NVIDIA NVLink',
          slug: 'understanding-nvidia-nvlink',
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
  label: 'GPU Instances',
  slug: 'gpu',
}
