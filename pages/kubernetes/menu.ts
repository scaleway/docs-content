export const kubernetesMenu = {
  items: [
    {
      label: 'Overview',
      slug: '../kubernetes',
    },
    {
      items: [
        {
          label: 'Introduction to Kubernetes',
          slug: 'introduction-to-kubernetes',
        },
        {
          label: 'Understanding differences between the Kapsule and Kosmos',
          slug: 'understanding-differences-kapsule-kosmos',
        },
        {
          label: 'Managed Kubernetes service definition',
          slug: 'managed-kubernetes-service-definition',
        },
        {
          label: 'Kubernetes control plane offers overview',
          slug: 'kubernetes-control-plane-offers',
        },
        {
          label: 'Kubernetes version support policy',
          slug: 'version-support-policy',
        },
        {
          label: 'Shared Responsibility Model for Kubernetes',
          slug: 'kubernetes-shared-responsibility-model',
        },
        {
          label: 'Glossary',
          slug: 'glossary',
        },        
      ],
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
          label: 'Create a Kapsule cluster',
          slug: 'create-cluster',
        },
        {
          label: 'Manage a Kapsule cluster',
          slug: 'edit-cluster',
        },
        {
          label: 'Manage Kapsule node pools',
          slug: 'manage-node-pools',
        },
        {
          label: 'Create a Kosmos cluster',
          slug: 'create-kosmos-cluster',
        },
        {
          label: 'Manage a Kosmos cluster',
          slug: 'edit-kosmos-cluster',
        },            
        {
          label:
            'Use the NVIDIA GPU operator on Kapsule and Kosmos with GPU Instances',
          slug: 'use-nvidia-gpu-operator',
        },
        {
          label: 'Access the Kubernetes dashboard',
          slug: 'access-kubernetes-dashboard',
        },
        {
          label: 'Upgrade the Kubernetes version on a Kapsule cluster',
          slug: 'upgrade-kubernetes-version',
        },
        {
          label: 'Deploy an image from Container Registry',
          slug: 'deploy-image-from-container-registry',
        },
        {
          label: 'Enable the Easy Deploy feature',
          slug: 'enable-easy-deploy',
        },
        {
          label: 'Use the Kapsule autoheal feature',
          slug: 'using-kapsule-autoheal-feature',
        },
        {
          label: 'Kubernetes kubectl Cheatsheet',
          slug: 'kubernetes-cheatsheet',
        },
        {
          label: 'Connect to a cluster with kubectl',
          slug: 'connect-cluster-kubectl',
        },
        {
          label: 'Create and manage a Kubernetes Kapsule with CLI v2',
          slug: 'creating-managing-kubernetes-lifecycle-cliv2',
        },
        {
          label: 'Change the control plane offer with CLI v2',
          slug: 'changing-control-plane-offer',
        },
        {
          label: 'Migrate end-of-life pools to newer Instances',
          slug: 'migrate-end-of-life-pools-to-newer-instances',
        },
        {
          label: 'Delete a cluster',
          slug: 'delete-cluster',
        },           
      ],
      label: 'Setup and lifecycle',
      slug: 'setup-lifecycle',
    },
    {
      items: [
        {
          label: 'Expose Kubernetes services to the internet',
          slug: 'exposing-services',
        },
        {
          label: 'Create and configure a Load Balancer service',
          slug: 'kubernetes-load-balancer',
        },
        {
          label: 'Manage Load Balancer IPs',
          slug: 'managing-load-balancer-ips',
        },
        {
          label: 'Use Load Balancer annotations',
          slug: 'using-load-balancer-annotations',
        },
        {
          label: 'Secure a cluster with Private Networks',
          slug: 'secure-cluster-with-private-network',
        },
        {
          label: 'Deploy an ingress controller',
          slug: 'deploy-ingress-controller',
        },
        {
          label: 'Use a Load Balancer with Ingress',
          slug: 'lb-ingress-controller',
        },
        {
          label: 'Wildcard DNS routing',
          slug: 'wildcard-dns',
        },
      ],
      label: 'Networking',
      slug: 'networking',
    },
    {
      items: [
        {
          label: 'Enable or disable SSH',
          slug: 'enable-disable-ssh',
        },
        {
          label: 'Set IAM permissions and implement RBAC on a cluster',
          slug: 'set-iam-permissions-and-implement-rbac',
        },
        {
          label: 'Configure Kubernetes security groups',
          slug: 'security-group-management',
        },
        {
          label: 'Deploy External Secrets on Kubernetes Kapsule',
          slug: 'external-secrets-kubernetes',
        },
        {
          label: 'Manage allowed IPs',
          slug: 'manage-allowed-ips',
        },
      ],
      label: 'Security',
      slug: 'security',
    },
    {
      items: [
        {
          label: 'Use File Storage with Kubernetes Kapsule',
          slug: 'use-sfs-with-kubernetes',
        },
        {
          label: 'Manage storage with CSI',
          slug: 'managing-storage',
        },
        {
          label: 'Use Kubernetes subPath with SFS on Kapsule',
          slug: 'using-subpath-with-sfs',
        },
        {
          label: 'Use scratch storage on H100 GPU Instances with Kapsule',
          slug: 'use-scratch-storage-h100',
        },
      ],
      label: 'Storage',
      slug: 'storage',
    },
    {
      items: [
        {
          label: 'Monitoring clusters',
          slug: 'cluster-monitoring',
        },
        {
          label: 'Monitor a Kapsule cluster with Cockpit',
          slug: 'monitor-cluster',
        },
        {
          label: "Monitor a cluster's data plane with Cockpit",
          slug: 'monitor-data-plane-with-cockpit',
        },
        {
          label: 'Access the Kubernetes audit logs',
          slug: 'access-audit-logs',
        },
      ],
      label: 'Observability',
      slug: 'observability',
    },
    {
      items: [
        {
          label: 'Ensuring resiliency with Multi-AZ clusters',
          slug: 'multi-az-clusters',
        },
        {
          label: 'Deploy x86 and ARM images in Kubernetes',
          slug: 'deploy-x86-arm-images',
        },
        {
          label: 'Recover ETCD database space for a cluster',
          slug: 'recover-space-etcd',
        },
        {
          label: 'Reach the API server via the VPC endpoint',
          slug: 'reach-api-server-via-vpc',
        },
        {
          label:
            'Modify kernel parameters in a Kubernetes cluster using a DaemonSet',
          slug: 'modifying-kernel-parameters-kubernetes-cluster',
        },
        {
          label: 'Manage tags',
          slug: 'managing-tags',
        },
      ],
      label: 'Advanced operations',
      slug: 'advanced-operations',
    },
    {
      items: [
        {
          label: 'Kubernetes API Reference',
          slug: 'https://www.scaleway.com/en/developers/api/kubernetes',
        },
      ],
      label: 'API',
      slug: 'api',
    },
    {
      label: 'FAQ',
      slug: 'faq',
    },
    {
      items: [
        {
          label: 'Containers are not starting on ARM Instances',
          slug: 'containers-not-starting-arm-instances',
        },
        {
          label:
            'Configuring a SQL storage backend in Helm on Scaleway Kubernetes Kapsule',
          slug: 'configuring-sql-storage-backend-helm',
        },
      ],
      label: 'Troubleshooting',
      slug: 'troubleshooting',
    },
  ],
  label: 'Kubernetes',
  slug: 'kubernetes',
}
