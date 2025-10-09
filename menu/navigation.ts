import { accountMenu } from '../pages/account/menu'
import { billingMenu } from '../pages/billing/menu'
import { environmentalFootprintMenu } from '../pages/environmental-footprint/menu'
import { iamMenu } from '../pages/iam/menu'
import { keyManagerMenu } from '../pages/key-manager/menu'
import { organizationsNProjectsMenu } from '../pages/organizations-and-projects/menu'
import { secretManagerMenu } from "../pages/secret-manager/menu"
import { generativeApisMenu } from "../pages/generative-apis/menu"
import { managedInferenceMenu } from "../pages/managed-inference/menu"
import { appleSiliconMenu } from "../pages/apple-silicon/menu"
import { ddxScwMenu } from "../pages/dedibox-scaleway/menu"
import { elasticMetalMenu } from "../pages/elastic-metal/menu"
import { instanceMenu } from '../pages/instances/menu'
import { gpuMenu } from "../pages/gpu/menu"
import { containerRegistryMenu } from "../pages/container-registry/menu"
import { kubernetesMenu } from "../pages/kubernetes/menu"
import { managedDatabasePostgresMySqlMenu } from "../pages/managed-databases-for-postgresql-and-mysql/menu"
import { managedDatabaseRedisMenu } from "../pages/managed-databases-for-redis/menu"
import { managedDatabaseMongoDbMenu } from "../pages/managed-mongodb-databases/menu"
import { openSearchMenu } from "../pages/opensearch/menu"
import { serverlessSqlDatabasesMenu } from "../pages/serverless-sql-databases/menu"
import { dataWarehouseMenu } from "../pages/data-warehouse/menu"
import { dataLabMenu } from "../pages/data-lab/menu"
import { natsMenu } from "../pages/nats/menu"
import { scwCliMenu } from "../pages/scaleway-cli/menu"
import { scwSdkMenu } from "../pages/scaleway-sdk/menu"
import { terraformMenu } from "../pages/terraform/menu"
import { domainsAndDnsMenu } from "../pages/domains-and-dns/menu"
import { transactionalEmailMenu } from "../pages/transactional-email/menu"
import { webHostingMenu } from "../pages/webhosting/menu"
import { iotHubMenu } from "../pages/iot-hub/menu"
import { topicsAndEventsMenu } from "../pages/topics-and-events/menu"
import { queuesMenu } from "../pages/queues/menu"
import { auditTrailMenu } from "../pages/audit-trail/menu"
import { cockpitMenu } from "../pages/cockpit/menu"
import { edgeServicesMenu } from "../pages/edge-services/menu"
import { interLinkMenu } from "../pages/interlink/menu"
import { ipamMenu } from "../pages/ipam/menu"
import { loadBalancersMenu } from "../pages/load-balancer/menu"
import { publicGatewaysMenu } from "../pages/public-gateways/menu"
import { vpcMenu } from "../pages/vpc/menu"
import { serverlessContainersMenu } from "../pages/serverless-containers/menu"
import { serverlessFunctionsMenu } from "../pages/serverless-functions/menu"
import { serverlessJobsMenu } from "../pages/serverless-jobs/menu"
import { blockStorageMenu } from "../pages/block-storage/menu"
import { fileStorageMenu } from "../pages/file-storage/menu"
import { localStorageMenu } from "../pages/local-storage/menu"
import { objectStorageMenu } from "../pages/object-storage/menu"
import { classicHostingMenu } from "../pages/classic-hosting/menu"
import { cpanelHostingMenu } from "../pages/cpanel-hosting/menu"
import { ddxAccountMenu } from "../pages/dedibox-account/menu"
import { ddxHardwareMenu } from "../pages/dedibox-hardware/menu"
import { ddxVpsMenu } from "../pages/dedibox-vps/menu"
import { ddxMenu } from "../pages/dedibox/menu"
import { ddxKvmOverIpMenu } from "../pages/dedibox-kvm-over-ip/menu"
import { ddxDomainsMenu } from "../pages/dedibox-domains/menu"
import { ddxDnsMenu } from "../pages/dedibox-dns/menu"
import { ddxIpFailoverMenu } from "../pages/dedibox-ip-failover/menu"
import { ddxIpv6Menu } from "../pages/dedibox-ipv6/menu"
import { ddxNetworkMenu } from "../pages/dedibox-network/menu"
import { ddxRpnMenu } from "../pages/dedibox-rpn/menu"
import { partnerSpaceMenu } from "../pages/partner-space/menu"

export default [
  {
    items: [
      {
        icon: 'OrganizationDashboardCategoryIcon',
        items: [
          accountMenu,
        ],
        label: 'Account',
        category: 'console',
      },
      {
        icon: 'CostAndImpactManagementCategoryIcon',
        items: [
          billingMenu,
          environmentalFootprintMenu
        ],
        label: 'Cost & Impact Management',
        category: 'console',
      },
      {
        icon: 'SecurityCategoryIcon',
        items: [
          iamMenu,
          keyManagerMenu,
          organizationsNProjectsMenu,
          secretManagerMenu,
        ],
        label: 'Security & Identity',
        category: 'identity-and-access-management',
      },
    ],
    label: 'Management & Governance',
  },
  {
    items: [
      {
        icon: 'AiCategoryIcon',
        items: [
          generativeApisMenu,
          managedInferenceMenu,
        ],
        label: 'AI',
        category: 'ai-data',
      },
      {
        icon: 'BaremetalCategoryIcon',
        items: [
          appleSiliconMenu,
          ddxScwMenu,
          elasticMetalMenu,
        ],
        label: 'Bare Metal',
        category: 'bare-metal',
      },
      {
        icon: 'ComputeCategoryIcon',
        items: [
          instanceMenu,
          gpuMenu,
        ],
        label: 'Compute',
        category: 'compute',
      },
      {
        icon: 'ContainersCategoryIcon',
        items: [
          containerRegistryMenu,
          kubernetesMenu,
        ],
        label: 'Containers',
        category: 'containers',
      },
      {
        icon: 'DatabaseCategoryIcon',
        items: [
          managedDatabasePostgresMySqlMenu,
          managedDatabaseRedisMenu,
          managedDatabaseMongoDbMenu,
          openSearchMenu,
          serverlessSqlDatabasesMenu,
        ],
        label: 'Databases',
        category: 'databases',
      },
      {
        icon: 'DataAndAnalyticsCategoryIcon',
        items: [
          dataWarehouseMenu,
          dataLabMenu,
          natsMenu,
        ],
        label: 'Data & Analytics',
        category: 'data-and-analytics',
      },
      {
        icon: 'DevToolsCategoryIcon',
        items: [
          scwCliMenu,
          scwSdkMenu,
          terraformMenu,
        ],
        label: 'Developer Tools',
        category: 'developer-tools',
      },
      {
        icon: 'DomainsAndWebHostingCategoryIcon',
        items: [
          domainsAndDnsMenu,
          transactionalEmailMenu,
          webHostingMenu,
        ],
        label: 'Domains & Web Hosting',
        category: 'domains-and-web-hosting',
      },
      {
        icon: 'IntegrationServicesCategoryIcon',
        items: [
          iotHubMenu,
          topicsAndEventsMenu,
          queuesMenu,
        ],
        label: 'Integration Services',
        category: 'integration-services',
      },
      {
        icon: 'MonitoringCategoryIcon',
        items: [
          auditTrailMenu,
          cockpitMenu,
        ],
        label: 'Monitoring',
        category: 'monitoring',
      },
      {
        icon: 'NetworkCategoryIcon',
        items: [
          edgeServicesMenu,
          interLinkMenu,
          ipamMenu,
          loadBalancersMenu,
          publicGatewaysMenu,
          vpcMenu,
        ],
        label: 'Network',
        category: 'network',
      },
      {
        icon: 'ServerlessComputeCategoryIcon',
        items: [
          serverlessContainersMenu,
          serverlessFunctionsMenu,
          serverlessJobsMenu,
        ],
        label: 'Serverless',
        category: 'serverless',
      },
      {
        icon: 'StorageCategoryIcon',
        items: [
          blockStorageMenu,
          fileStorageMenu,
          localStorageMenu,
          objectStorageMenu,
        ],
        label: 'Storage',
        category: 'storage',
      },
    ],
    label: 'Products',
  },
  {
    items: [
      {
        icon: 'OrganizationDashboardCategoryIcon',
        items: [
          classicHostingMenu,
          cpanelHostingMenu,
          ddxAccountMenu,
        ],
        label: 'Dedibox Console',
        category: 'dedibox-console',
      },
      {
        icon: 'DedicatedServerCategoryIcon',
        items: [
          ddxHardwareMenu,
          ddxMenu,
          ddxVpsMenu,
          ddxKvmOverIpMenu
        ],
        label: 'Dedibox Servers',
        category: 'dedibox',
      },
      {
        icon: 'NetworkCategoryIcon',
        items: [
          ddxDomainsMenu,
          ddxDnsMenu,
          ddxIpFailoverMenu,
          ddxIpv6Menu,
          ddxNetworkMenu,
          ddxRpnMenu,
        ],
        label: 'Dedibox Network',
        category: 'dedibox-network',
      },
    ],
    label: 'Dedibox',
  },
  {
    items: [
      {
        icon: 'PartnersCategoryIcon',
        items: [
          partnerSpaceMenu,
        ],
        label: 'Partners',
        category: 'partners',
      },
    ],
    label: 'Additional Services',
  },
]
