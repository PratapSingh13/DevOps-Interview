# Kubernetes Security Best Practices

We have often misconception that **I'm on cloud and I'm secure**. But, it's not true. 

### Kubernetes security by default
- How secure is kubernetes by default?
- What are the security gaps?
- What are the security best practices to close those gaps?

## 1. Image Scanning

As we run our containers from images, so building the secure image in our CI/CD pipeline is the first step to secure our application.

**What security issues do we have here?**
- Images are built in layers and each layer can have command or configuration etc. 
    - Code from untrusted sources (may include malicious code)
    - Vulnarabilities in tools of OS or libraries (may be base image that we are using is having vulnarabilities). By this attacker can read data in host's volumes, read from file system, read kubelet configuration.

**Best Practices**
- Use minimal base images
- Use distroless images
- Use image scanning

## 2. Run as non-root user

If we have vulnerabilty with image amd running with root privilage then attacker can exploit it and can get root access to the node. 

**Best Practices**
- Run as non-root user
- Run as non-root group
- Run as dedicated user and group

## 3. Users & Permissions with RBAC

Keep privilages as **restrictive as possible!**

## 4. Network Policies

Network policies are used to control the traffic between pods.

**Best Practices**
- Use network policies to control the traffic between pods
- Use network policies to control the traffic between pods and services
- Use network policies to control the traffic between pods and external services

## 5. Secrets Management

Secrets management is used to store sensitive information in Kubernetes.

**Best Practices**
- Use secrets management to store sensitive information in Kubernetes




---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png