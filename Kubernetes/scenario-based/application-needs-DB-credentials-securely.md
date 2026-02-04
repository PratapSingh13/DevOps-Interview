**An application needs DB credentials securely. How will you store and inject secrets in Kubernetes?**

**Answer-** I store DB credentials in **Kubernetes Secrets** (or an external secret manager) and inject them into pods using **environment variables or mounted volumes**, while restricting access using **RBAC**, encryption at rest, and secret rotation.

#### 1️⃣ Where to Store Secrets

**✅ Option 1: Kubernetes Secrets (Baseline)**

Create a Secret (base64-encoded):

```bash
kubectl create secret generic db-secret \
  --from-literal=DB_USER=appuser \
  --from-literal=DB_PASSWORD=strongpassword \
  -n app-ns
```

**✅ Option 2: External Secret Managers (Best Practice – Production)**

**Use:**
- Cloud secret managers (AWS/GCP/Azure)
- HashiCorp Vault

Then sync secrets into Kubernetes using:
- External Secrets Operator
- CSI Secrets Store Driver

✔ Better security
✔ Central rotation
✔ Audit logs

#### 2️⃣ How to Inject Secrets into Pods

**🔹 Method A: Environment Variables (Most Common)**

```yaml
env:
- name: DB_USER
  valueFrom:
    secretKeyRef:
      name: db-secret
      key: DB_USER
- name: DB_PASSWORD
  valueFrom:
    secretKeyRef:
      name: db-secret
      key: DB_PASSWORD
```

**Pros**
- Simple
- Widely supported

**Cons**
- Requires pod restart on secret change
- Visible in the process environment

**🔹 Method B: Secret as Volume (More Secure)**

```yaml
volumes:
- name: db-secret
  secret:
    secretName: db-secret

volumeMounts:
- name: db-secret
  mountPath: /etc/secrets
  readOnly: true
```

**Application reads:**

```bash
/etc/secrets/DB_PASSWORD
```

**Pros**
- Auto-updates when secret changes
- Not exposed as env vars

**Cons**
- App must read files

#### 3️⃣ Secret Rotation Strategy

- Rotate secrets in the external secret manager
- Sync updated secrets automatically
- Restart pods (or rely on volume updates)

✔ No hardcoded credentials
✔ Zero manual intervention

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
