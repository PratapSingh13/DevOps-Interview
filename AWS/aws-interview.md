- **What is difference between LoadBalancers?**
  ALB — Layer 7 (HTTP/HTTPS traffic), Flexible.
  NLB — Layer 4 (TLS/TCP/UDP traffic), Static IPs.
  CLB — Layer 4/7 (HTTP/TCP/SSL traffic), Legacy, Avoid.  

  - With ALB, it is a requirement that you enable at least two or more Availability Zones.
  