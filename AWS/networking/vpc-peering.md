# About AWS VPC Peering

**AWS VPC Peering** allows you to connect two or more VPCs privately using AWS internal network, enabling resources in one VPC to communicate with resources in the other VPC without traversing the internet.

### Key Points

- VPC Peering is a **regional service**
- VPC Peering is **not transitive** (if VPC A is peered with VPC B, and VPC B is peered with VPC C, VPC A cannot communicate with VPC C through VPC B)
- VPC Peering is **not recursive** (if VPC A is peered with VPC B, and VPC B is peered with VPC C, VPC A cannot communicate with VPC C through VPC B)
- CIDR blocks must NOT overlap (❌ Overlapping CIDRs → peering not allowed)

**Note-** Use VPC Peering for simple, small-scale connectivity; use Transit Gateway for large, multi-VPC architectures.

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png

