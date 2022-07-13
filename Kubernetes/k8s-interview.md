- **What is Kubernetes?**

  Kubernetes is an open-source container management tool that holds the responsibilities of container deployment, scaling & descaling of containers & load balancing.

- **How is Kubernetes different from Docker Swarm?**

|**Features**                   | **Kubernetes** | **Docker Swarm** |
|:-----------------------------:|:----------:|:-----------------:|
| **Installation & Cluster Config** | Setup is very complicated, but once installed cluster is robust. | Installation is very simple, but the cluster is not robust.|
| **GUI** | GUI is the Kubernetes Dashboard. | There is no GUI.|
| **Scalability** | Highly scalable and scales fast. | Highly scalable and scales 5x faster than Kubernetes. |
| **Auto-scaling** | Kubernetes can do auto-scaling. | Docker swarm cannot do auto-scaling. |
| **Load Balancing** | Manual intervention needed for load balancing traffic between different containers and pods.	 | Docker swarm does auto load balancing of traffic between containers in the cluster. |
| **Rolling Updates & Rollbacks** | Can deploy rolling updates and does automatic rollbacks. | Can deploy rolling updates, but not automatic rollback. |
| **Logging & Monitoring** | In-built tools for logging and monitoring.	| 3rd party tools like ELK stack should be used for logging and monitoring.|

- **What are the features of Kubernetes**

![](../images/k8s-features.png)

- **How does Kubernetes simplify containerized Deployment?**

  As a typical application would have a cluster of containers running across multiple hosts, all these containers would need to talk to each other. So, to do this you need something big that would load balance, scale & monitor the containers. Since Kubernetes is cloud-agnostic and can run on any public/private providers it must be your choice simplify containerized deployment.

- **Can you brief on the working of the master node in Kubernetes?**

  Kubernetes master controls the nodes and inside the nodes the containers are present. Now, these individual containers are contained inside pods and inside each pod, you can have a various number of containers based upon the configuration and requirements. So, if the pods have to be deployed, then they can either be deployed using user interface or command-line interface. Then, these pods are scheduled on the nodes, and based on the resource requirements, the pods are allocated to these nodes. The kube-apiserver makes sure that there is communication established between the Kubernetes node and the master components.

  ![](../images/k8s-masterNode.png)

- **What is the role of kube-apiserver and kube-scheduler?**

**kube – apiserver** follows the scale-out architecture and, is the front-end of the master node control panel. This exposes all the APIs of the Kubernetes Master node components and is responsible for establishing communication between Kubernetes Node and the Kubernetes master components.

**kube-scheduler** is responsible for the distribution and management of workload on the worker nodes. So, it selects the most suitable node to run the unscheduled pod based on resource requirement and keeps a track of resource utilization. It makes sure that the workload is not scheduled on nodes that are already full.

- **What is Kubernetes controller manager?**

  Multiple controller processes run on the master node but are compiled together to run as a single process which is the Kubernetes Controller Manager. So, Controller Manager is a daemon that embeds controllers and does namespace creation and garbage collection. It owns the responsibility and communicates with the API server to manage the end-points.

  ![](../images/k8s-controllManager.png)

- **What is ETCD?**

  Etcd is written in Go programming language and is a distributed key-value store used for coordinating distributed work. So, Etcd stores the configuration data of the Kubernetes cluster, representing the state of the cluster at any given point in time.

- **What is Ingress network, and how does it work?**

  Ingress network is a collection of rules that acts as an entry point to the Kubernetes cluster. This allows inbound connections, which can be configured to give services externally through reachable URLs, load balance traffic, or by offering name-based virtual hosting. So, Ingress is an API object that manages external access to the services in a cluster, usually by HTTP and is the most powerful way of exposing service.

  
- **What is Liveness Probe and Readiness Probe**

  Liveness and Readiness probes are used to control the health of an application running inside a Pod’s container. Both of them are very similar in functionality, and usage.

  **Liveness Probe-** Suppose that a Pod is running our application inside a container, but due to some reason let’s say memory leak, cpu usage, application deadlock etc the application is not responding to our requests, and stuck in error state.

  Liveness probe checks the container health as we tell it do, and if for some reason the liveness probe fails, it restarts the container.

  **Readiness Probe-** In some cases we would like our application to be alive, but not serve traffic unless some conditions are met e.g, populating a dataset, waiting for some other service to be alive. In such cases we use readiness probe. If the condition inside readiness probe passes, only then our application can serve traffic.
 
- **What is ClusterIP,  NodePort,  Ingress and  LoadBalancer?**
   
  - Using Kubernetes proxy and ClusterIP: The default Kubernetes ServiceType is ClusterIp, which exposes the Service on a cluster-internal IP. To reach the ClusterIp from an external source, you can open a Kubernetes proxy between the external source and the cluster. This is usually only used for development.

  - Exposing services as NodePort: Declaring a Service as NodePortexposes it on each Node’s IP at a static port (referred to as the NodePort). You can then access the Service from outside the cluster by requesting <NodeIp>:<NodePort>. This can also be used for production, albeit with some limitations.
  default range of nodeport is 30000-32767

  - Exposing services as LoadBalancer: Declaring a Service as LoadBalancer exposes it externally, using a cloud provider’s load balancer solution. The cloud provider will provision a load balancer for the Service, and map it to its automatically assigned NodePort. This is the most widely used method in production environments.

- **What is Ingress?**
  Ingress isn’t a type of Service, but rather an object that acts as a reverse proxy and single entry-point to your cluster that routes the request to different services. The most basic Ingress is the NGINX Ingress Controller, where the NGINX takes on the role of reverse proxy, while also functioning as SSL.

- **What is difference between ReplicaSet and ReplicationController?**
  Replica Set and Replication Controller do almost the same thing. Both of them ensure that a specified number of pod replicas are running at any given time. The difference comes with the usage of selectors to replicate pods. Replica Set use Set-Based selectors while replication controllers use Equity-Based selectors.


### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://github.com/PratapSingh13
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png