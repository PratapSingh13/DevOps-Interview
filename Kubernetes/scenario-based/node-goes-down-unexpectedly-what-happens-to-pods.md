**One worker node goes down unexpectedly. What happens to the pods, and how does Kubernetes recover?**

**Answer-** When a worker node goes down, Kubernetes marks it NotReady, removes its pods from service endpoints, evicts them after a grace period, and recreates them on healthy nodes using controllers like Deployments or StatefulSets. With autoscaling enabled, new nodes are added automatically if capacity is insufficient.

### 🔁 What Happens Internally (Step-by-Step)

#### 1️⃣ Node Becomes Unreachable

- The kubelet on the node stops responding.
- The control plane marks the node as NotReady.

#### 2️⃣ Kubernetes Waits (Grace Period)

- Kubernetes does **not immediately delete pods**

**Default timings:**

- node-monitor-grace-period ≈ 40s
- pod-eviction-timeout ≈ 5 minutes

👉 This avoids flapping during transient network issues.

#### 3️⃣ Pods on That Node Are Marked Unknown

- Pod status becomes Unknown
- Pods are not serving traffic anymore

**If a Service is used:**
- Traffic is automatically removed from these pods

#### 4️⃣ Controller Manager Evicts Pods

**After eviction timeout:**
- Pods are deleted
- Controllers step in:
  - Deployment
  - ReplicaSet
  - StatefulSet
  - DaemonSet (special case)
 
#### 5️⃣ Pods Are Rescheduled on Healthy Nodes

- Scheduler places new pods on available nodes
- New pods go through:
  - Image pull
	- Startup
	- Readiness checks
 
 ### 🧱 What About Storage?

**🔹 Stateless Pods**
- No impact
- Full recovery

**🔹 Stateful Pods (PVCs)**
- Pod reattaches volume on new node
- Requires storage that supports reattachment (EBS, etc.)

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
