# Loadbalancer vs Ingress

### LoadBalancer

**A Kubernetes Service type that exposes one service externally using a cloud provider’s L4 load balancer.**

**Load Balancer:** A kubernetes LoadBalancer service is a service that points to external load balancers that are NOT in your kubernetes cluster, but exist elsewhere. They can work with your pods, assuming that your pods are externally routable. Google and AWS provide this capability natively. In terms of Amazon, this maps directly with ELB and kubernetes when running in AWS can automatically provision and configure an ELB instance for each LoadBalancer service deployed.

```
Client
  |
Cloud Load Balancer (L4)
  |
Service (LoadBalancer)
  |
Pods
```

**Key Characteristics**
* Works at Layer 4 (TCP/UDP)
* One LoadBalancer per Service
* Gets a public IP
* Simple and fast

```yml
apiVersion: v1
kind: Service
metadata:
  name: backend-svc
spec:
  type: LoadBalancer
  ports:
    - port: 80
      targetPort: 8080
  selector:
    app: backend
```

**Pros**

✅ Simple to set up \
✅ Good for non-HTTP protocols (DB, TCP, gRPC*)\
✅ No extra components needed 


**Cons**

❌ Expensive (one LB per service) \
❌ No path/host routing \
❌ Limited TLS handling

### Ingress

**An API object that defines HTTP/HTTPS routing rules, implemented by an Ingress Controller.**

**Ingress:** An ingress is really just a set of rules to pass to a controller that is listening for them. You can deploy a bunch of ingress rules, but nothing will happen unless you have a controller that can process them. A LoadBalancer service could listen for ingress rules, if it is configured to do so.

```
Client
  |
Ingress Controller (L7)
  |
Ingress Rules
  |
Services
  |
Pods
```

**Key Characteristics**
* Works at Layer 7 (HTTP/HTTPS)
* One LB → many services
* Supports host/path-based routing
* Handles TLS termination

```yml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
spec:
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-svc
            port:
              number: 80
```

**Pros**

✅ Cost-effective \
✅ Path & host routing \
✅ Centralized TLS \
✅ Ideal for web apps

**Cons**

❌ HTTP/HTTPS only \
❌ Requires Ingress Controller \
❌ Advanced features need annotations

**When to Use What?**

**Use LoadBalancer when:**
* You need TCP/UDP traffic
* You expose databases or non-HTTP services
* You want simplicity

**Use Ingress when:**
* You expose web applications
* You need HTTPS, path routing
* You want cost optimization

```Ingress is being replaced by Gateway API for advanced use cases.```
