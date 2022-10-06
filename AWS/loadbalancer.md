- **What is difference between LoadBalancers?**
  ALB — Layer 7 (HTTP/HTTPS traffic), Flexible.
  NLB — Layer 4 (TLS/TCP/UDP traffic), Static IPs.
  CLB — Layer 4/7 (HTTP/TCP/SSL traffic), Legacy, Avoid.  

  - With ALB, it is a requirement that you enable at least two or more Availability Zones.
  
- **How can I assign a role to the user in AWS?**

  To assign IAM role to an IAM user, do the following:
  
  - Open the IAM Dashboard
  - Select the role that you want to assign to an IAM user
  - Edit the trust policy
  - Add the ARN of the IAM user in the Principal's section