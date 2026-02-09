**An application pod keeps restarting with CrashLoopBackOff. What steps will you follow to identify and fix the issue?**

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

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png