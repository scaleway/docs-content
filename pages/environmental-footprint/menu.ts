export const environmentalFootprintMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../environmental-footprint',
    },
    {
      label: 'Concepts',
      slug: 'concepts',
    },
    {
      label: 'FAQ',
      slug: 'faq',
    },
    {
      items: [
         {
          label: 'Use the Environmental Footprint dashboard',
          slug: 'environmental-footprint-dashboard',
        },
        {
          label: 'Track your monthly environmental footprint report',
          slug: 'track-monthly-footprint',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Calculation breakdown',
          slug: 'environmental-footprint-calculator',
        },
        {
          label: 'Calculation reference values',
          slug: 'calculation-values-reference',
        },
        {
          label: 'Calculator product integration',
          slug: 'environmental-footprint-integration',
        },
        {
          label:
            'Understanding your environmental footprint estimation',
          slug: 'environmental-footprint-calculator-estimation',
        },
        {
          label: 'Bare Metal footprint calculation',
          slug: 'bare-metal-env-footprint',
        },
        {
          label: 'Instances footprint calculation',
          slug: 'instances-env-footprint',
        },
        {
          label: 'Block Storage footprint calculation',
          slug: 'block-storage-env-footprint',
        },
        {
          label: 'Object Storage footprint calculation',
          slug: 'object-storage-env-footprint'
        },
        {
          label: 'Load Balancer footprint calculation',
          slug: 'load-balancer-env-footprint'
        }
      ],
      label: 'Additional Content',
      slug: 'additional-content',
    },
  ],
  label: 'Environmental Footprint',
  slug: 'environmental-footprint',
}
