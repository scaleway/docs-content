const expectedTypes = ['feat', 'fix', 'test', 'build', 'refactor', 'docs'];
const expectedProducts = ['APS','AUT','BIL','BLS','CPT','ACC','CR','DDX',
                        'DTO','DOM','EM','ESE','FDB','GEN','GPU','IAM','INS',
                        'IOT','K8S','LRN','LB','MAS','MNQ','NET','S3','RDB','VPC',
                        'PGW','RED','SEM','SRV','SDB','SRV','TEM','UAPI','VPC','WH'];

module.exports = {
  extends: ['@commitlint/config-conventional'],
  plugins: [
        {
            rules: {
                'custom-type-enum': ({ type }) => {
                if (!expectedTypes.includes(type)) {
                    return [false,
                    `
                    Commit message must be in the following format:\n

                    "type(product): subject"\n

                    Type must be one of the following:\n
                    ${expectedTypes.join(', ')} \n
                    Scope must be a product acronym: 

                    Example: 
                    "docs(INS): add new documentation page"
                                `];
                    }
                return [true];
                 },
                'custom-type-enum': ({ product }) => {
                if (!expectedProducts.includes(product)) {
                    return [false,
                        `
                        Commit message must be in the following format:\n
                        
                        "type(product): subject"\n
                        
                        Product must be one of the following:\n
                        
                        Apple Silicon - APS       | Auth - AUT                  | Billing - BIL              | Block storage - BLS
                        Cockpit - CPT             | Account - ACC               | Container Registry - CR    | Dedibox - DDX
                        Developer tools - DTO     | Domains and DNS - DOM       | Elastic Metal - EM         | Edge Services - ESE
                        General - GEN             | GPU - GPU                   | IAM - IAM                  | Instances - INS 
                        IoT Hub - IOT             | Kubernetes - K8S            | Learning - LRN             | Load Balancer - LB      
                        Managed Services - MAS    | Messaging & Queuing - MNQ   | Network products - NET     | Object Storage - S3     
                        PostgreSQL - MySQL - RDB  | Private networks - VPC      | Public Gateway - PGW       | Redis™ - RED
                        Secret Manager - SEM      | Serverless Containers - SRV | Serverless Databases - SDB | Serverless Funct - SRV
                        Transactional Email - TEM | Users and API - UAPI        | Virtual Private Cloud - VPC| Web hosting - WH
                        Scope must be a product acronym: 
                        
                        Example: 
                        "docs(INS): add new documentation page"
                        `];
                    }
                    return [true];
                },
            },
        },
  ],
  rules: {
    'custom-type-enum': [2, 'always'],
  },
};
