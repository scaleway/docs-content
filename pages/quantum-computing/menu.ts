export const quantumComputingMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../quantum-computing',
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
          label: 'Use Quandela QPUs & emulators',
          slug: 'use-quandela-qpus',
        },
        {
          label: 'Use Pasqal QPUs & emulators',
          slug: 'use-pasqal-qpus',
        },
        {
          label: 'Use IQM QPUs & emulators',
          slug: 'use-iqm-qpus',
        },
        {
          label: 'Use AQT QPUs & emulators',
          slug: 'use-aqt-qpus',
        },
        {
          label: 'Use remote Aer emulators',
          slug: 'use-aer-emulators',
        },
        {
          label: 'Use remote Qsim emulators',
          slug: 'use-qsim-emulators',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Containers API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/qaas/',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
  ],
  label: 'Quantum Computing',
  slug: 'quantum-as-a-service',
}
