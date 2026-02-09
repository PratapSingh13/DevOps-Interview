**You need to deploy a new version without downtime. Which deployment strategy will you use and why?**

**Answer-** For zero downtime, I primarily use Rolling Updates with strict readiness probes and maxUnavailable set to zero. For high-risk or high-traffic releases, I prefer Blue-Green or Canary deployments to ensure safe rollout and instant rollback.

#### 1️⃣ Rolling Update

**Why choose it?**

- Native Kubernetes support
- Zero downtime when configured correctly
- No extra infrastructure needed

**How it works**
- Gradually replaces old pods with new ones
- Keeps service available throughout

**Key configuration**

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 0
    maxSurge: 1
```
**Why this works**
- maxUnavailable: 0 ensures availability
- Readiness probes prevent bad pods from receiving traffic

✔ Best for stateless services

#### 2️⃣ Blue-Green Deployment

Why choose it?
- Full validation before exposing users
- Rollback is immediate

How it works
- Run blue (current) and green (new) versions in parallel
- Switch traffic via Service or Ingress

Example
- Service initially points to app=v1
- After validation → switch to app=v2

✔ Ideal for critical business apps

❌ Needs double resources temporarily

#### 3️⃣ Critical Requirements for Zero Downtime

**✔ Readiness Probes**

Only send traffic to ready pods.

**✔ Proper Graceful Shutdown**

```yaml
terminationGracePeriodSeconds: 30
```

**✔ Backward-Compatible APIs**

Old and new versions must coexist briefly.

**✔ Pod Disruption Budget**

```yaml
minAvailable: 80%
```

---
 
### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png