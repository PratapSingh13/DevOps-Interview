## 🧩 Beginner / Foundation Scenarios

**1. A pod is stuck in the Pending state. How will you troubleshoot? What are the possible causes?**
   
**Answer-** A pod in Pending means **Kubernetes has accepted the pod, but it has not been scheduled onto any node.**

### 🏆 One-Line Summary (For Interviews)

A pod remains in Pending state when the scheduler cannot find a suitable node due to resource shortages, scheduling constraints, storage issues, or policy restrictions. The fastest way to diagnose is by checking pod events using ```kubectl describe pod```.

### 🔍 Step-by-Step Troubleshooting Approach
**1️⃣ Check Pod Events**
```bash
kubectl describe pod <pod-name> -n <namespace>
```
👉 Look at the Events section at the bottom. **This usually tells you exactly why scheduling failed.**

#### ⚠️ Common Causes & How to Identify Them

🔹 **Insufficient Cluster Resources (CPU / Memory)**

**Symptom in events:**
```
0/5 nodes are available: insufficient cpu / insufficient memory
```
#### How to fix:

•	Reduce resource requests \
•	Add more nodes \
•	Enable Cluster Autoscaler

🔹 **Node Selector / Affinity Mismatch**
**Symptom in events:**
```
node(s) didn't match node selector
```

#### Why it happens:

•	Pod has nodeSelector, nodeAffinity, or podAffinity rules \
•	No node matches the required labels

```bash
kubectl get nodes --show-labels
```

**Fix:**

•	Update pod selectors \
•	Add correct labels to nodes

```bash
kubectl label node <node-name> env=prod
```

🔹 **Taints and Tolerations Issue**

**Symptom:**
```
node(s) had taint {key=value:NoSchedule}
```

#### Why it happens:

•	Node is tainted \
•	Pod does not tolerate the taint

**Check taints:**
```bash
kubectl describe node <node-name>
```
**Fix (add toleration):**
```yaml
tolerations:
- key: "dedicated"
  operator: "Equal"
  value: "frontend"
  effect: "NoSchedule"
```

🔹 **PersistentVolumeClaim (PVC) Not Bound**

**Symptom:**
```
pod has unbound immediate PersistentVolumeClaims
```

Why it happens:

•	PVC exists but no matching PV \
•	StorageClass misconfigured

**Check**
```bash
kubectl get pvc
kubectl get pv
```

**Fix:**

•	Create PV \
•	Fix StorageClass \
•	Ensure correct access mode & size

🔹 **Pod Requests Special Resources**

**Examples:**

•	GPUs \
•	HugePages \
•	Custom device plugins

**Symptom:**
```
Insufficient nvidia.com/gpu
```

**Fix:**

•	Add suitable nodes \
•	Reduce special resource requests

🔹 **Namespace ResourceQuota Limit Reached**

**Symptom:**
```
exceeded quota
```

**Check:**
```bash
kubectl describe quota -n <namespace>
```

**Fix:**

•	Increase quota \
•	Reduce pod requests

---

**2. An application pod keeps restarting with CrashLoopBackOff. What steps will you follow to identify and fix the issue?**
**Answer-** The container is repeatedly crashing shortly after starting. Kubernetes attempts to restart the container, but it fails again, creating a loop where the time between restarts increases exponentially (10s, 20s, 40s... up to 5 minutes) to avoid overloading the node. 

### 🔍 Step-by-Step Troubleshooting Approach

#### 1️⃣ Identify the Exact Failure Reason

**Check pod status & events**

```bash
kubectl describe pod <pod-name> -n <namespace>
```

**Focus on:**
- Last state
- Exit code
- Events

```
Last State: Terminated
Reason: Error
Exit Code: 1
```

#### 2️⃣ Check Application Logs

**Current container logs**

```bash
kubectl logs <pod-name> -n <namespace>
```

**Previous crashed container logs**

```bash
kubectl logs <pod-name> -n <namespace> --previous
```

#### 3️⃣ Identify the Root Cause Category

**🔹 A. Misconfiguration**
- Missing environment variables
- Wrong config values
- App fails to bind to port
- Dependency not reachable (DB, API)

**🔹 B. Wrong Container Command or Entrypoint**

```
exec: "start.sh": no such file or directory
```

**🔹 C. Liveness / Readiness Probe Misconfiguration**

**Fix:**
- Increase initialDelaySeconds
- Fix probe path/port
- Use readiness probe first

**🔹 D. OOMKilled (Memory Issues)**

```
Reason: OOMKilled
Exit Code: 137
```

**Fix:**
- Increase memory limits
- Fix memory leak
- Adjust JVM / runtime memory flags

**🔹 E. Missing Dependencies (ConfigMap / Secret / Volume)**

**Fix:**
- Ensure volume mounts exist
- Correct file paths
- Architecture mismatch (amd64 vs arm64)

---

**3. Pods are running, but the application is not accessible via the Service. What will you check?**
**Answer-** The Service exists, but traffic is not correctly reaching the pods or the application inside the pods.

### 🔍 Step-by-Step Troubleshooting Flow

#### 1️⃣ Verify Pod Health & Readiness

Even if pods are running, they may not be Ready.

```bash
kubectl get pods -n <namespace>
```

**Check readiness probe:**

```bash
kubectl describe pod <pod-name>
```

**Fix:**
- Correct readiness probe path/port
- Increase initialDelaySeconds

👉 If the pod is not Ready, Service will NOT send traffic to it.

#### 2️⃣ Check Service Selectors

 ```bash
kubectl describe svc <service-name> -n <namespace>
```

**Verify:**

```yaml
selector:
  app: my-app
```

**Compare with pod labels:**

```bash
kubectl get pods --show-labels
```

❌ **If labels don’t match → Service has no endpoints**

#### 3️⃣ Check Service Endpoints

```bash
kubectl get endpoints <service-name> -n <namespace>
```

**Possible outcomes:**
- ❌ No endpoints → selector mismatch/pod not Ready
- ✅ Endpoints exist → move to networking checks

#### 4️⃣ Validate Target Port vs Container Port

**Service:**

```yaml
ports:
- port: 80
  targetPort: 8080
```

**Pod:**

```yaml
containerPort: 8080
```

**❌ Mismatch = traffic dropped**

#### 5️⃣ Test Connectivity Inside the Cluster

**Exec into another pod:**

```bash
kubectl exec -it <test-pod> -- curl http://<service-name>:<port>
```

**If this fails:**
- Service misconfiguration
- Network policy blocking traffic

#### 6️⃣ Check Application Binding

**Application must listen on:**

```code
0.0.0.0
```

**❌ If app binds to localhost (127.0.0.1) → Service cannot reach it**

#### 7️⃣ Check Network Policies
#### 8️⃣ Check kube-proxy / CNI Issues
