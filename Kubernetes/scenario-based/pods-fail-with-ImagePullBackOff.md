**Pods fail with ImagePullBackOff. What are the common reasons and resolutions?**

**Answer-** ImagePullBackOff occurs when Kubernetes cannot pull the container image due to wrong image names, authentication issues, network problems, or node constraints. I diagnose it via pod events and resolve it by fixing image references, registry access, or node configuration.

### 🔍 Step-by-Step Troubleshooting Approach

**1️⃣ Check Pod Events**
```bash
kubectl describe pod <pod-name> -n <namespace>
```
Look at **Events**, for example:

```code
Failed to pull image "repo/app:v1"
unauthorized: authentication required
```
#### ⚠️ Common Reasons & How to Fix Them

**🔹 Wrong Image Name or Tag**

**🔹 Private Registry Authentication Issue**

**Symptoms:**

```code
unauthorized: authentication required
```
**Why**
- Missing or incorrect imagePullSecret

**Fix:**

```bash
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<password>
```

**Attach to pod:**

```yaml
imagePullSecrets:
- name: regcred
```

**🔹 Image Registry Unreachable (Network / DNS)**

**Symptoms:**

```code
i/o timeout
connection refused
```
**Why**
- No internet access
- Firewall / proxy issue
- DNS resolution failure

**🔹 Image Architecture Mismatch**

**Why**
- Image built for amd64, node is arm64

**Fix:**
- Build multi-arch image

```bash
docker buildx build --platform linux/amd64,linux/arm64
```

**🔹 Docker Hub Rate Limiting**

---
