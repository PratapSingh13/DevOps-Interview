# Kubernetes architecture overview

- K8 nodes are divided into 2 types, master node(control plane), and worker node
- These nodes can be a physical machines as well as the virtual machines
- Master and Worker nodes have different components resided inside it

## Master Node

- Master is responsible for managing the complete cluster.
- You can access master node via the CLI, GUI, or API.
- The master watches over the nodes in the cluster and is responsible for the actual orchestration of containers on the worker nodes.
- For achieving fault tolerance, there can be more than one master node in the cluster.
- It is the access point from which administrators and other users interact with the cluster to manage the scheduling and deployment of containers.
- It has four components: ETCD, Scheduler, Controller and API Server

### Master Node (Control Plane) components
- API Server
- ETCD
- Control Manager
- Scheduler

### Worker Node Components
- Kubelet
- kube-proxy
- Container Runtime

#### Kubernetes Master server components

**API Server**

- It basically redirects all the API to a particular component, for example, if we wish to create a pod, then our request is received by the API server, and then it will forward it to the control manager.
- End-user only will talk to API server only.
- The API server will also authenticate and authorize the user
- Masters communicate with the rest of the cluster through the kube-apiserver, the main access point to the control plane.
- It validates and executes user's REST commands
kube-apiserver also makes sure that configurations in etcd match with configurations of containers deployed in the cluster

**ETCD**

- ETCD is a distributed reliable key-value store used by Kubernetes to store all data used to manage the cluster.
- It is a database for k8, data is stored in the form of key-value pair.
- it has data of nodes, config, secret, accounts, role binding, replica set, replica controller, RBAC, etc.
- When you have multiple nodes and multiple masters in your cluster, etcd stores all that information on all the nodes in the cluster in a distributed manner.
- ETCD is responsible for implementing locks within the cluster to ensure there are no conflicts between the Masters

**Control Manager**

- The controllers are the brain behind orchestration.
- They are responsible for noticing and responding when nodes, containers or endpoints goes down.
- The controllers makes decisions to bring up new containers in such cases.
- The kube-controller-manager runs control loops that manage the state of the cluster by checking if the required deployments, replicas, and nodes are running in the cluster   

**Scheduler**

- Scheduler task is to schedule the tasks(like creating pod) on the proper node, it checks for the highest ram and storage available node and schedules the tasks accordingly, it basically manages the load between the nodes.
- It looks for newly created containers and assigns them to Nodes.

#### Kubernetes Worker node components

**Kubelet**

- Worker nodes have the kubelet agent that is responsible for interacting with the master to provide health information of the worker node
- To carry out actions requested by the master on the worker nodes.
- Kublet's task is to create the pod and monitor its status and provide the report to the API server.
- It will only manage containers which are created by k8 only


**Kube-proxy**

- Kube proxy will create and manage the network rules, it will help to establish communication between two pods which are in different nodes
- The kube-proxy is responsible for ensuring network traffic is routed properly to internal and external services as required and is based on the rules defined by network policies in kube-controller-manager and other custom controllers.

**Container Runtime**

- Container Runtime is a software that is responsible for running the containers on the worker node.
- It basically tells the node what to do, for example, if we wish to create a pod, then our request is received by the API server, and then it will forward it to the control manager, which will then forward it to the kubelet on the node where the pod is to be created.

---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png