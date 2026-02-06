# About NAT Gateway

**NAT Gateway**, also known as **Network Address Translation Gateway**, is used to enable instances present in a private subnet to help connect to the internet or AWS services.

### Key Points

- NAT Gateway must be in a public subnet
- Public subnet must have:
  - Route to IGW
  - Elastic IP attached to NAT Gateway

### 🧭 Routing Configuration (Very Important)

**Private Subnet Route Table**

```code
0.0.0.0/0 → NAT Gateway
```

**Public Subnet Route Table**

```code
0.0.0.0/0 → IGW
```

### 🏷️ NAT Gateway vs NAT Instance

| Feature | NAT Gateway | NAT Instance |
| --- | --- | --- |
| **Managed by AWS** | Yes | No |
| **High Availability** | Yes (AZ scoped) | No (single AZ) |
| **Scalability** | Automatic | Manual |
| **Cost** | Higher | Lower |
| **Performance** | Better | Lower |
| **Maintenance** | None | Required |


---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png