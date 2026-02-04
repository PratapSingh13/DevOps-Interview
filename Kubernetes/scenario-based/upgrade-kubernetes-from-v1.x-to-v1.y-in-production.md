**You need to upgrade Kubernetes from v1.x to v1.y in production. What precautions and steps will you follow?**

**Answer-** A Kubernetes upgrade is not just a version bump.
It involves **API compatibility, control plane safety, node draining, workload disruption, and rollback planning.**

### 1️⃣ Pre-Upgrade Precautions

#### ✅ Check Kubernetes Version Skew Policy
- Control plane must be upgraded before nodes
- kubelet can be ±1 minor version only

✔ Prevents cluster instability

#### ✅ Review Deprecated & Removed APIs 

```bash
kubectl get apiservices
```

**Check:**
- Deprecated APIs in v1.x
- Removed APIs in v1.y

**Examples:**
- extensions/v1beta1
- policy/v1beta1

❌ If workloads use removed APIs → upgrade will break

✔ Fix manifests before upgrade

#### ✅ Audit Cluster Add-Ons Compatibility

**Verify compatibility for:**

- CNI (Calico / Cilium / AWS VPC CNI)
- CoreDNS
- kube-proxy
- Ingress controller
- Metrics Server
- CSI drivers

👉 Most upgrade failures happen here, not in core K8s.

#### ✅ Backup & Rollback Plan (NON-NEGOTIABLE)
- Backup etcd (or ensure managed control plane backup)
- Export manifests:

```bash
kubectl get all -A -o yaml > cluster-backup.yaml
```

### 2️⃣ Prepare the Workloads

#### ✅ Ensure High Availability
- Multiple replicas
- PodDisruptionBudgets in place

✔ Prevents downtime during node drains

#### ✅ Freeze Deployments (Change Control)
- No application releases during upgrade

### 3️⃣ Test the Upgrade First (ABSOLUTELY REQUIRED)

#### ✅ Non-Prod / Staging Cluster
- Same Kubernetes version
- Same add-ons
- Same workloads

✔ If it fails here → do NOT upgrade prod

### 4️⃣ Upgrade the Control Plane (FIRST)

**Why first?**
- Control plane is backward compatible with older nodes
- Nodes are NOT forward compatible with newer control plane indefinitely

**Control plane upgrade:**
- Causes no workload restart
- API server briefly unavailable

✔ Safe if workloads are HA

### 5️⃣ Upgrade Worker Nodes (ONE BY ONE)

**Step-by-Step Node Upgrade Pattern**

```bash
kubectl cordon <node>
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
```

- Upgrade kubelet & OS
- Restart node

```bash
kubectl uncordon <node>
```

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
