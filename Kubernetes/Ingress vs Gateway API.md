# Ingress vs Gateway API

## Ingress

**Ingress** is a Kubernetes resource that defines **rules for routing external HTTP/HTTPS traffic** to services inside a Kubernetes cluster.

It works at **Layer 7 (HTTP)** and needs an **Ingress Controller (like NGINX or ALB)** to actually handle the traffic.

**Key points for ingress**
* Works only for HTTP/HTTPS
* Uses host-based and path-based routing
* Requires an Ingress Controller
* One ingress can route traffic to multiple services
* Older and limited for advanced use cases


**Problems with Ingress**
* No support for multi-tenancy
* No support for Namespace isolation
* No RBAC for features
* No resource isolation
* No support for CORS

## Gateway API

**Gateway API** is a **Kubernetes networking API** that defines **how traffic enters, exits, and moves inside a Kubernetes cluster** in a **standard and extensible way** it works on **Layer-4 and Layer-7**.

It is designed to replace Ingress and solve its limitations by:
* Supporting multiple protocols
* Providing clean separation of responsibilities
* Offering fine-grained traffic control

**Why Gateway API Was Needed (Problem It Solves)**

**Problems with Ingress**
* HTTP only
* Heavy use of annotations
* Hard to manage in multi-team environments
* No standard way to do TCP, gRPC, or advanced routing

**Gateway API Fixes This By**
* Defining clear APIs instead of annotations
* Supporting HTTP, TCP, UDP, gRPC
* Separating infra config from app routing

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png
