export const loadBalancerMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../load-balancer',
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
          label: 'Create a Load Balancer',
          slug: 'create-load-balancer',
        },
        {
          label: 'Create frontends and backends',
          slug: 'create-frontends-backends',
        },
        {
          label: 'Manage frontends and backends',
          slug: 'manage-frontends-and-backends',
        },
        {
          label: 'Add an SSL/TLS certificate',
          slug: 'add-certificate',
        },
        {
          label: 'Create and manage ACLs',
          slug: 'create-manage-acls',
        },
        {
          label: 'Create and manage routes',
          slug: 'create-manage-routes',
        },
        {
          label: 'Use a Load Balancer with a Private Network',
          slug: 'use-with-private-network',
        },
        {
          label: 'Set up an Edge Services pipeline',
          slug: 'use-edge-services',
        },
        {
          label: 'Set up a customized error page',
          slug: 'set-up-s3-failover',
        },
        {
          label: 'Create and manage flexible IPs',
          slug: 'create-manage-flex-ips',
        },
        {
          label: 'Resize a Load Balancer',
          slug: 'resize-lb',
        },
        {
          label: 'Monitor your Load Balancer with Scaleway Cockpit',
          slug: 'monitor-lb-cockpit',
        },
        {
          label: 'Delete a Load Balancer',
          slug: 'delete-load-balancer',
        },
      ],
      label: 'How to',
      slug: 'how-to',
    },
    {
      items: [
        {
          label: 'Load Balancer API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/load-balancer/zoned-api/',
        },
        {
          label: 'Setting up SSL offloading',
          slug: 'setting-up-ssl-offloading',
        },
        {
          label: 'Configuring balancing rules',
          slug: 'configuring-balancing-rules',
        },
      ],
      label: 'API/CLI',
      slug: 'api-cli',
    },
    {
      items: [
        {
          label: 'Configuring frontends',
          slug: 'configuring-frontends',
        },
        {
          label: 'Configuring backends',
          slug: 'configuring-backends',
        },
        {
          label: 'Configuring health checks',
          slug: 'configuring-health-checks',
        },
        {
          label: 'Setting up SSL bridging, offloading or passthrough',
          slug: 'ssl-bridging-offloading-passthrough',
        },
        {
          label: 'Setting up your Load Balancer for HTTP/2 or HTTP/3',
          slug: 'http2-http3',
        },
        {
          label: 'Understanding ACLs',
          slug: 'acls',
        },
        {
          label: 'Kubernetes Load Balancers',
          slug: 'kubernetes-load-balancer',
        },
        {
          label: 'Public vs private Load Balancers',
          slug: 'public-private-accessibility',
        },
        {
          label: 'Migrating from AWS ELB',
          slug: 'migrating-aws',
        },
        {
          label: 'Deprecation of SNI routes with HTTP backends',
          slug: 'sni-route-deprecation',
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
  label: 'Load Balancers',
  slug: 'load-balancer',
}
