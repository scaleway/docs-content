// please use precise camel case versions of each product slug
// for its associated menu naming, to avoid breaking tooling
import { accountMenu } from '../pages/account/menu'
import { appleSiliconMenu } from "../pages/apple-silicon/menu"
import { auditTrailMenu } from "../pages/audit-trail/menu"
import { billingMenu } from '../pages/billing/menu'
import { blockStorageMenu } from "../pages/block-storage/menu"
import { classicHostingMenu } from "../pages/classic-hosting/menu"
import { cockpitMenu } from "../pages/cockpit/menu"
import { containerRegistryMenu } from "../pages/container-registry/menu"
import { cpanelHostingMenu } from "../pages/cpanel-hosting/menu"
import { dataLabMenu } from "../pages/data-lab/menu"
import { dataWarehouseMenu } from "../pages/data-warehouse/menu"
import { dediboxMenu } from "../pages/dedibox/menu"
import { dediboxAccountMenu } from "../pages/dedibox-account/menu"
import { dediboxDnsMenu } from "../pages/dedibox-dns/menu"
import { dediboxDomainsMenu } from "../pages/dedibox-domains/menu"
import { dediboxHardwareMenu } from "../pages/dedibox-hardware/menu"
import { dediboxIpFailoverMenu } from "../pages/dedibox-ip-failover/menu"
import { dediboxIpv6Menu } from "../pages/dedibox-ipv6/menu"
import { dediboxKvmOverIpMenu } from "../pages/dedibox-kvm-over-ip/menu"
import { dediboxNetworkMenu } from "../pages/dedibox-network/menu"
import { dediboxRpnMenu } from "../pages/dedibox-rpn/menu"
import { dediboxScalewayMenu } from "../pages/dedibox-scaleway/menu"
import { dediboxVpsMenu } from "../pages/dedibox-vps/menu"
import { domainsAndDnsMenu } from "../pages/domains-and-dns/menu"
import { edgeServicesMenu } from "../pages/edge-services/menu"
import { elasticMetalMenu } from "../pages/elastic-metal/menu"
import { environmentalFootprintMenu } from '../pages/environmental-footprint/menu'
import { fileStorageMenu } from "../pages/file-storage/menu"
import { generativeApisMenu } from "../pages/generative-apis/menu"
import { gpuMenu } from "../pages/gpu/menu"
import { iamMenu } from '../pages/iam/menu'
import { instancesMenu } from '../pages/instances/menu'
import { interlinkMenu } from "../pages/interlink/menu"
import { iotHubMenu } from "../pages/iot-hub/menu"
import { ipamMenu } from "../pages/ipam/menu"
import { keyManagerMenu } from '../pages/key-manager/menu'
import { kubernetesMenu } from "../pages/kubernetes/menu"
import { loadBalancerMenu } from "../pages/load-balancer/menu"
import { localStorageMenu } from "../pages/local-storage/menu"
import { managedDatabasesForPostgresqlAndMysqlMenu } from "../pages/managed-databases-for-postgresql-and-mysql/menu"
import { managedDatabasesForRedisMenu } from "../pages/managed-databases-for-redis/menu"
import { managedInferenceMenu } from "../pages/managed-inference/menu"
import { managedMongodbDatabasesMenu } from "../pages/managed-mongodb-databases/menu"
import { natsMenu } from "../pages/nats/menu"
import { objectStorageMenu } from "../pages/object-storage/menu"
import { openSearchMenu } from "../pages/opensearch/menu"
import { organizationsAndProjectsMenu } from '../pages/organizations-and-projects/menu'
import { partnerSpaceMenu } from "../pages/partner-space/menu"
import { publicGatewaysMenu } from "../pages/public-gateways/menu"
import { queuesMenu } from "../pages/queues/menu"
import { scalewayCliMenu } from "../pages/scaleway-cli/menu"
import { scalewaySdkMenu } from "../pages/scaleway-sdk/menu"
import { secretManagerMenu } from "../pages/secret-manager/menu"
import { serverlessContainersMenu } from "../pages/serverless-containers/menu"
import { serverlessFunctionsMenu } from "../pages/serverless-functions/menu"
import { serverlessJobsMenu } from "../pages/serverless-jobs/menu"
import { serverlessSqlDatabasesMenu } from "../pages/serverless-sql-databases/menu"
import { terraformMenu } from "../pages/terraform/menu"
import { topicsAndEventsMenu } from "../pages/topics-and-events/menu"
import { transactionalEmailMenu } from "../pages/transactional-email/menu"
import { vpcMenu } from "../pages/vpc/menu"
import { webhostingMenu } from "../pages/webhosting/menu"

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
          organizationsAndProjectsMenu,
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
          dediboxScalewayMenu,
          elasticMetalMenu,
        ],
        label: 'Bare Metal',
        category: 'bare-metal',
      },
      {
        icon: 'ComputeCategoryIcon',
        items: [
          instancesMenu,
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
          managedDatabasesForPostgresqlAndMysqlMenu,
          managedDatabasesForRedisMenu,
          managedMongodbDatabasesMenu,
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
          scalewayCliMenu,
          scalewaySdkMenu,
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
          webhostingMenu,
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
          interlinkMenu,
          ipamMenu,
          loadBalancerMenu,
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
          dediboxAccountMenu,
        ],
        label: 'Dedibox Console',
        category: 'dedibox-console',
      },
      {
        icon: 'DedicatedServerCategoryIcon',
        items: [
          dediboxHardwareMenu,
          dediboxMenu,
          dediboxVpsMenu,
          dediboxKvmOverIpMenu
        ],
        label: 'Dedibox Servers',
        category: 'dedibox',
      },
      {
        icon: 'NetworkCategoryIcon',
        items: [
          dediboxDomainsMenu,
          dediboxDnsMenu,
          dediboxIpFailoverMenu,
          dediboxIpv6Menu,
          dediboxNetworkMenu,
          dediboxRpnMenu,
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
