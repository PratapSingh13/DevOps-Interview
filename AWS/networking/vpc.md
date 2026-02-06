# About VPC

## 🌐 What is AWS VPC?

A **VPC (Virtual Private Cloud)** is a **logically isolated virtual network** inside AWS where you launch AWS resources with full control over:
- IP addressing
- Subnets
- Routing
- Security
- Internet / private connectivity

**Note-** VPC is region scoped service in AWS.

#### 🧱 Core VPC Components

**1️⃣ CIDR Block (IP Range)**

- Defines IP space of VPC

```code
10.0.0.0/16
```

**Rules:**
- Cannot overlap with other VPCs (if peering)
- Cannot be changed later (only extended)

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png