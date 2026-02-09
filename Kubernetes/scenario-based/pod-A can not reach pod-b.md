**Pod-A cannot reach Pod-B — how do you troubleshoot?**

**Answer-** I troubleshoot pod-to-pod connectivity by checking pod status, DNS resolution, service configuration, network policies, CNI health, and namespace isolation—moving from application layer down to networking.

#### 1️⃣ Confirm both pods are actually running

```bash
kubectl get pods -A -o wide
```

**Expected Output:**

```
NAME      STATUS    ROLES    AGE    IP           NODE
pod-a     Running   <none>   5m     10.244.1.2   node-1
pod-b     Running   <none>   5m     10.244.2.3   node-2
```

Check:
- STATUS = Running
- Pods scheduled on different nodes? (important later)

If Pod-B is:
- CrashLoopBackOff
- NotReady
➡️ Network is not the issue yet

#### 2️⃣ Verify Pod-B is listening on the expected port

From **inside Pod-B:**

```bash
kubectl exec -it pod-b -- netstat -tulnp
```

Common mistake:
- App listens on localhost instead of 0.0.0.0

❌ Localhost → unreachable from other pods

✅ 0.0.0.0 → reachable from all pods

#### 3️⃣ Test direct Pod IP connectivity

From **Pod-A:**

```bash
kubectl exec -it pod-a -- curl <POD-B-IP>:<PORT>
```

Results:
- ❌ Fails → network or policy issue
- ✅ Works → Service/DNS issue

#### 4️⃣ If using Service, check Service & endpoints

```bash
kubectl get svc
kubectl get endpoints <service-name>
```

❌ Empty endpoints = readiness probe failing
❌ Wrong port mapping = connection refused

#### 5️⃣ Check DNS resolution

From **Pod-A:**

```bash
kubectl exec -it pod-a -- nslookup pod-b
kubectl exec -it pod-a -- nslookup service-name
```

If DNS fails:
- CoreDNS issue
- Wrong namespace
- Using short name instead of FQDN

Correct DNS format:

```code
service-name.namespace.svc.cluster.local
```

#### 6️⃣ Namespace mismatch

✅ Use:

```bash
service-name.other-namespace.svc.cluster.local
```

#### 7️⃣ Check NetworkPolicies

```bash
kubectl get networkpolicy -A
```

If **any NetworkPolicy** exists in the namespace:

- Default behavior becomes deny
- Explicit allow rules required

#### 8️⃣ Verify CNI plugin health

In Kubernetes, pod-to-pod traffic is handled by CNI.

Check CNI pods:

```bash
kubectl get pods -n kube-system -l k8s-app=calico-node
```

If CNI is broken → no pod networking at all

#### 9️⃣ Check Node-to-Node Connectivity

If pods are on different nodes, check routing:

```bash
# From node where pod-a runs
telnet <POD-B-IP> <PORT>
```

If this fails:
- Check node firewall
- Check Calico/Flannel routing rules
- Check node security groups (cloud)

#### 🔟 Check kube-proxy Health

```bash
kubectl get pods -n kube-system -l k8s-app=kube-proxy
```

kube-proxy handles Service IP routing.


### 🎯 Quick Troubleshooting Checklist

1. **Pods Running?** → `kubectl get pods -A`
2. **Listening on 0.0.0.0?** → `kubectl exec pod-b -- netstat -tulnp`
3. **Direct IP Reachable?** → `kubectl exec pod-a -- curl <IP>`
4. **Service Exists?** → `kubectl get svc`
5. **Endpoints Healthy?** → `kubectl get endpoints <service>`
6. **DNS Working?** → `kubectl exec pod-a -- nslookup pod-b`
7. **NetworkPolicy Blocking?** → `kubectl get networkpolicy -A`
8. **CNI Healthy?** → `kubectl get pods -n kube-system -l k8s-app=calico-node`
9. **Node Routing OK?** → `telnet <IP> <PORT>` from node
10. **Kube-proxy Running?** → `kubectl get pods -n kube-system -l k8s-app=kube-proxy`

---

### 💡 Common Pitfalls

- ❌ App listening on localhost
- ❌ Missing Service endpoints
- ❌ NetworkPolicy blocking traffic
- ❌ DNS resolution issues
- ❌ CNI plugin not running
- ❌ Node-level firewall blocking
- ❌ Wrong namespace
- ❌ Readiness probe failing

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png