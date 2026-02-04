**Pods in different namespaces cannot communicate. How will you debug networking issues?**

**Answer-** By default, Kubernetes allows cross-namespace pod-to-pod communication.
If communication fails, it is almost always due to **NetworkPolicies, DNS issues, or CNI misconfiguration.**

### 🏆 One-Line Summary (For Interviews)

Since Kubernetes allows cross-namespace traffic by default, I first verify service endpoints and DNS, then inspect NetworkPolicies for deny rules, validate namespace labels, and finally check CNI plugin health to isolate the issue.

### 🔍 Step-by-Step Troubleshooting Approach

#### 1️⃣ Confirm the Problem from Inside the Cluster

**Test connectivity from Pod A → Pod B**

```bash
kubectl exec -it pod-a -n ns-a -- curl http://service-b.ns-b:8080
```

**Also test:**

```bash
nslookup service-b.ns-b
```

✔ Confirms whether it’s **DNS or network path**

#### 2️⃣ Verify the Service Exists & Endpoints Are Ready

```bash
kubectl get svc service-b -n ns-b
kubectl get endpoints service-b -n ns-b
```

❌ No endpoints = pod selector / readiness issue
✔ Endpoints present = move to policy checks

#### 3️⃣ Check NetworkPolicies

```bash
kubectl get networkpolicy -A
```

**Look for:**
- Default deny ingress
- Default deny egress

**Fix: Allow Cross-Namespace Traffic Explicitly**

```yaml
ingress:
- from:
  - namespaceSelector:
      matchLabels:
        name: ns-a
```

#### 4️⃣ Check Pod-Level Readiness
- Pod must be Ready
- Non-ready pods don’t receive traffic

#### 5️⃣ Verify Application Is Listening Correctly

**Inside Pod B:**

```bash
netstat -tuln
```

✔ App must listen on 0.0.0.0, not 127.0.0.1

#### 6️⃣ Check CNI Plugin Health (Advanced)

```bash
kubectl get pods -n kube-system
```

**Look for:**
- Calico
- Cilium
- Flannel

❌ Crashed CNI = broken networking

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
