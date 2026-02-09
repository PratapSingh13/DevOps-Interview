**Users complain about high latency but CPU/memory look fine. What Kubernetes-level metrics will you check?**

**Answer-** Latency issues are often caused by **networking, load balancing, scheduling, or application readiness,** not raw CPU or memory usage.

### 🔍 Kubernetes-Level Metrics I Will Check

#### 1️⃣ Request & Response Latency Metrics (TOP PRIORITY)

**At Service / Ingress Level**
- P95 / P99 latency
- Request duration histogram
- Error rate (4xx / 5xx)

#### 2️⃣ Pod Readiness & Endpoint Health

**Metrics:**
- Number of Ready vs NotReady pods
- Endpoint count vs desired replicas

**Why:**
- Fewer ready pods → traffic overload on remaining pods
- Causes queueing and slow responses

#### 3️⃣ Request Queue & Concurrency

#### 4️⃣ Network-Level Metrics

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
