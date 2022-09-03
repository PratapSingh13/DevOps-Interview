# Kubernetes — Service Types Overview

There are four types of Kubernetes services — ```ClusterIP, NodePort, Headless, LoadBalancer and ExternalName```.

**1.  ClusterIP**
    
-   ClusterIP is the default and most common service type. It means when we do not specify any service in ```type``` then by default kubernetes understand of ClusterIP service.

-   Kubernetes will assign a cluster-internal IP address to ClusterIP service. This makes the service only reachable within the cluster.

-   You cannot make requests to service (pods) from outside the cluster.

**Use Cases**

-   Inter service communication within the cluster. For example, communication between the front-end and back-end components of your app.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app-service
  namespace: learning
  
spec:
  selector: 
    app: my-app-service
    type: backend
  type: ClusterIP     # Optional field (default) 
  ports:
    - name: http
      protoco;: TCP
      port: 80
      targetPort: 8080
```

**2. NodePort**

-   A NodePort is an open port on every node of your cluster. Kubernetes transparently routes incoming traffic on the NodePort to your service, even if your application is running on a different node.

-   NodePort service is an extension of ClusterIP service. A ClusterIP Service, to which the NodePort Service routes, is automatically created.

-   It exposes the service outside of the cluster by adding a cluster-wide port on top of ClusterIP.

-   NodePort ranges (typically 30000–32767)

**3. Headless**

-   Client wants to communicate 1 specific pod directly then for this we use **Headless Service**

-   Pods wants to talk directly specific pod

-   Use case is for Stateless application like databases.

**4.  LoadBalancer**
-   Using a LoadBalancer service type automatically deploys an external load balancer. This external load balancer is associated with a specific IP address and routes external traffic to a Kubernetes service in your cluster.

-   The exact implementation of a LoadBalancer is dependent on your cloud provider, and not all cloud providers support the LoadBalancer service type.




### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png