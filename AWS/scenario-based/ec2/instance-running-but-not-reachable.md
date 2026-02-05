**An EC2 instance is running but not reachable. What could be the reasons?**

**Answer-** If an EC2 instance is running but not reachable, I first check **networking (public IP, route table, IGW), then security (security group and NACL), followed by OS-level issues like SSH service, disk space, or CPU exhaustion.** I also verify EC2 status checks and use SSM or EC2 Instance Connect for recovery if direct SSH is not possible.

### 🔍 Step-by-Step Troubleshooting Approach

#### 1️⃣ Instance & AWS Health Checks

**Goal:** Confirm instance state

✔ **Instance state:** Running
✔ **System Status Check:** Passed
✔ **Instance Status Check:** Passed

**If failed:**
- System check failed → AWS host issue → **Stop/Start or Recover**
- Instance check failed → OS issue → **SSM / volume recovery**

#### 2️⃣ Identify Connectivity Type

**Goal:** Are you connecting via public or private access?
🔹 Public access → Internet → EC2
🔹 Private access → Bastion / VPN / Direct Connect

#### 3️⃣ Network Layer Issues

**❌ No Public IP / Elastic IP**
- Instance in public subnet but no public IP attached
- Elastic IP not associated

**✅ Fix:**
Attach a public IP or use **Elastic IP**

**❌ Route Table Misconfiguration**
- 0.0.0.0/0 not routed to Internet Gateway

**✅ Fix:**
Ensure the route table has:

```code
0.0.0.0/0 → igw-xxxxxxxx
```

**❌ Internet Gateway Missing**
- VPC has no IGW attached

**✅ Fix:**
Attach an **IGW** to the **VPC**

#### 4️⃣ Security Layer Issues

**❌ Security Group Blocking Traffic**
- SSH (22) / HTTP (80) / HTTPS (443) not allowed
- Source IP not allowed

**✅ Fix:**
Allow required ports from the correct CIDR:

```code
SSH → 22 → Your IP
HTTP → 80 → 0.0.0.0/0
```

**❌ Network ACL Blocking Traffic**
- Inbound or outbound rules deny traffic

#### 5️⃣ OS / Instance-Level Issues

**❌ Disk Full or CPU Exhausted**
- Root disk full → SSH fails
- CPU at 100%

**✅ Fix:**
- Check via EC2 System Logs
- Increase disk or instance size

#### 6️⃣ AWS Health & Status Checks

**❌ Failing EC2 Status Checks**
- System status check failure → AWS infrastructure issue
- Instance status check failure → OS issue

**✅ Fix:**
- Stop/start instance
- Recover instance
- Rebuild from AMI

---
### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
