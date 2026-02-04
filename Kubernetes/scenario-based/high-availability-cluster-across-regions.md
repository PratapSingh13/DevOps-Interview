**You need high availability across regions. How will you design Kubernetes architecture?**

**Answer-** Kubernetes **does not support multi-region clusters natively** in a reliable way.
For true regional HA, I will design **multiple clusters (one per region)** and handle traffic, data, and failover externally.

### 🧠 High-Level Architecture

```code
Users
  ↓
Global DNS / Traffic Manager
  ↓
Region A Kubernetes Cluster (AZ multi-node)
  ↓
Region B Kubernetes Cluster (AZ multi-node)
```

**Each region is:**
- Fully independent
- Multi-AZ inside the region
- Able to serve traffic on its own

#### 1️⃣ Multi-Cluster, Multi-Region Design

**Why not a single cluster?**
- etcd latency across regions
- Control plane instability
- Network partitions

**Correct approach:**
- One Kubernetes cluster per region
- Same application deployed to all clusters

✔ Independent scaling
✔ Safer upgrades

#### 2️⃣ Traffic Management

**Option A: Active–Active**
- Both regions serve live traffic
- Traffic split using:
- Geo-based routing
- Latency-based routing
- Weighted routing

```code
app.example.com
 ├── ALB-ap-south-1 (EKS India)
 └── ALB-us-east-1 (EKS US)
```

**Benefits:**
- Lowest latency
- No cold standby
- Instant failover

**Option B: Active–Passive**
- Primary region handles traffic
- Secondary is on standby
- DNS failover on health check failure

```code
Route 53 Failover Routing
 ├── Primary ALB (EKS-A)
 └── Secondary ALB (EKS-B)
```

**Tradeoff:**
- Slight downtime during failover
- Simpler data handling

#### 3️⃣ Ingress & Load Balancing per Region

**Each cluster has:**
- Internal Kubernetes Service
- Regional Ingress / Load Balancer


#### 4️⃣ Configuration & Deployment Consistency
- Same manifests across regions
- Environment-specific configs
- Automated pipelines deploy to all clusters

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
