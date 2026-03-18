#  1. Networking & Edge

| **Service** | **Surface Level** | **Architecture Clarity** | **Operational Depth** | **Troubleshooting Maturity** |
|-------------|-------------------|--------------------------|-----------------------|------------------------------|
| **VPC** | Logical network in AWS | CIDR planning, subnet segmentation, multi-AZ HA | IP exhaustion planning, subnet sizing | Overlapping CIDR causing peering failure |
| **Subnets** | Public vs Private | NAT vs IGW traffic flow | CIDR fragmentation planning | Instance has no internet → route/NAT issue |
| **Route Tables** | Control traffic routing | TGW propagation vs static routes | Multi-account route management | Traffic drop due to wrong target| 
| **Security Groups** | Stateful firewall | App-tier isolation model | Least privilege ingress | Port open but still blocked? Check NACL |
| **NACLs** | Stateless filter | Rare but used in strict compliance | Rule ordering logic | Deny rule precedence issues |
| **Internet Gateway** | Public internet access | IGW vs NAT Gateway decision | Multi-AZ IGW design | IGW not in Route Table |
| **NAT Gateway** | Outbound internet for private subnet | Cost-heavy component in architecture | AZ-wise NAT placement | Private EC2 can’t reach internet |
| **Transit Gateway** | Connect multiple VPCs | Hub-spoke multi-account network | Route table association/propagation | Overlapping CIDR failure |
| **VPC Peering** | Connect two VPCs | One-to-one VPC connection | No transitive routing | Overlapping CIDR failure |
| **VPC Endpoints** | Private AWS service access | Reduce NAT cost | Interface endpoint security groups | S3 access denied due to endpoint policy |
| **CloudFront** | CDN | Edge caching + origin design | TTL tuning | Cache invalidation delay |
| **Route 53** | DNS service | Failover routing, weighted routing | Health check configs | DNS propagation delay |


#  2. Compute Layer
| **Service** | **Surface Level** | **Architecture Clarity** | **Operational Depth** | **Troubleshooting Maturity** |
|-------------|-------------------|--------------------------|-----------------------|------------------------------|
| **EC2** | Virtual Machine | Stateless vs Stateful design | AMI Lifecycle, Launch templates | CPU steal, memory pressure |
| **Auto Scaling** | Scale EC2 automatically | Horizontal elasticity pattern | Target tracking vs step scaling | Scaling not triggering? Check metrics |
| **ECS** | Container orchestration | Fargate vs EC2 tradeoff | Task definition revision mgmt | Task stuck in provisioning |
| **EKS** | Managed Kubernetes | Control plane vs worker nodes | IRSA, CNI, node groups | Pod can’t reach service |
| **Lambda** | Serverless compute | Event-driven microservices | Concurrency tuning | Cold start + timeout errors |
| **Batch** | Batch workloads | Spot-heavy cost optimization | Retry strategies | Job stuck in RUNNABLE |

# 3. IAM & Security
| **Service** | **Surface Level** | **Architecture Clarity** | **Operational Depth** | **Troubleshooting Maturity** |
|-------------|-------------------|--------------------------|-----------------------|------------------------------|
| **IAM** | Users, Roles, Policies | Policy evaluation logic | Cross-account role assumption | AccessDenied root cause tracing |
| **STS** | Temporary credentials | Federation architecture | Token expiration handling | AssumeRole failing |
| **KMS** | Encryption key mgmt | Envelope encryption model | CMK rotation | KMS throttling |
| **Secrets Manager** | Store secrets | Secret rotation architecture | Lambda rotation function | App failing due to expired secret |
| **SSM Parameter Store** | Config storage | SecureString vs String | Hierarchical structure | EC2 not fetching param |
| **WAF** | Web firewall | ALB integration | Rule priority tuning | Legit traffic blocked |
| **GuardDuty** | Threat detection | Central security account model | Finding severity mgmt | False positives analysis |
| **Organizations** | Multi-account mgmt | Landing zone design | SCP governance | SCP blocking prod access |

# 4. Storage & Databases
| **Service** | **Surface Level** | **Architecture Clarity** | **Operational Depth** | **Troubleshooting Maturity** |
|-------------|-------------------|--------------------------|-----------------------|------------------------------|
| **S3** | Object storage | Data lake, static hosting | Lifecycle + replication | Access denied bucket policy |
| **EBS** | Block storage | AZ bound | Snapshot automation | Volume stuck in attaching |
| **EFS** | Shared filesystem | Multi-AZ storage | Throughput modes | Mount target not reachable |
| **RDS** | Managed DB | Multi-AZ HA | Backup retention | Connection timeout |
| **DynamoDB** | NoSQL DB | Serverless scaling | Capacity mode tuning | Throttling exception |
| **ElastiCache** | Redis cache | Caching layer pattern | TTL strategy | Cache miss storm |

# 5. Load Balancing & API Layer
| **Service** | **Surface Level** | **Architecture Clarity** | **Operational Depth** | **Troubleshooting Maturity** |
|-------------|-------------------|--------------------------|-----------------------|------------------------------|
| **ALB** | L7 load balancer | Path-based routing | Listener rules mgmt | 502/503 errors |
| **NLB** | L4 load balancer | High-performance TCP | Static IP requirement | Target unhealthy |
| **API Gateway** | Managed API layer | Auth + throttling | Rate limit mgmt | 429 throttling errors |

# 6. Observability & Governance
| **Service** | **Surface Level** | **Architecture Clarity** | **Operational Depth** | **Troubleshooting Maturity** |
|-------------|-------------------|--------------------------|-----------------------|------------------------------|
| **CloudWatch** | Metrics + logs | Centralized monitoring | Alarm strategy | Metric not emitted |
| **CloudTrail** | API audit | Security logging | Organization trail | Event missing |
| **X-Ray** | Distributed tracing | Microservice tracing | Sampling tuning | Latency root cause |
| **AWS Config** | Compliance tracking | Drift detection | Rule automation | Non-compliant resource |

