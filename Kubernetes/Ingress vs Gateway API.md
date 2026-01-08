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

## Gateway API

**Gateway API** is a **Kubernetes networking API** that defines **how traffic enters, exits, and moves inside a Kubernetes cluster** in a **standard and extensible way**.

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
