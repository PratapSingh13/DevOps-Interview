# About Subnet

## 🌐 What is Subnet in AWS VPC?

A subnet is a **CIDR block within a VPC** that exists in a single Availability Zone and is used to place AWS resources with specific routing and security requirements

**Note-** Subnet is AZ scoped service in AWS.

### 🏷️ Public vs Private Subnet

**❌ Subnets are not public or private by nature; they become public or private based on their route table**

#### 🌍 Public Subnet

A subnet with a route to an **Internet Gateway (IGW)**.

#### 🔒 Private Subnet

A subnet without a route to an **Internet Gateway (IGW)**.

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png