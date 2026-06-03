## You updated a ConfigMap, but the application still uses old values. Why is this happening, and how do you fix it?

**Answer-** ConfigMap updates are not automatically propagated to running containers when they are consumed as environment variables or when the application does not reload configuration dynamically.

### 🏆 One-Line Summary (For Interviews)

ConfigMap changes don’t automatically reflect in running pods because environment variables are static and applications often don’t reload configs. The fix is restarting pods, using volume mounts with reload logic, or triggering restarts via checksum annotations.

### 🔍 Step-by-Step Troubleshooting Approach

#### 1️⃣ ConfigMap Used as Environment Variables

**Example**

```yaml
envFrom:
- configMapRef:
    name: app-config
```

**Why it happens:**
- Environment variables are read only at container startup
- Updating ConfigMap does NOT update env vars in running pods

#### 2️⃣ Application Does Not Reload Config Files

**Example:**

```yaml
volumeMounts:
- name: config
  mountPath: /etc/config
```

**Even though Kubernetes updates the mounted file:**
- Application may cache config in memory
- App does not watch file changes

#### 3️⃣ Pods Were Not Restarted
- Kubernetes does not restart pods automatically on ConfigMap change
- Old pods keep running with old config

#### 4️⃣ Wrong ConfigMap or Namespace
- ConfigMap updated in different namespace
- Pod still points to old ConfigMap name

#### 5️⃣ Immutable ConfigMap
```yaml
immutable: true
```

- Updates are silently ignored
- Requires deletion & recreation

### 🛠️ How to Fix It

#### ✅ Fix 1: Restart Pods

```bash
kubectl rollout restart deployment <deployment-name> -n <namespace>
```
✔ Forces pods to reload updated config

#### ✅ Fix 2: Use ConfigMap as Volume + App Reload Logic
```yaml
volumes:
- name: config
  configMap:
    name: app-config
```

✔ Kubernetes updates files automatically \
❌ App must reload config or support SIGHUP

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
