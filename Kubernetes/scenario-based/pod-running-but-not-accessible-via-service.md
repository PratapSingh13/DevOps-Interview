**Pods are running, but the application is not accessible via the Service. What will you check?**

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

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png