# Pods

Pods are the smallest, most basic deployable object in Kubernetes.

Pods contains one or more containers, such as Docker containers. When a Pod runs multiple containers, the containers are managed as a single entity and share the Pod's resources. Generally, running multiple containers in a single Pod is an advanced use case.

Pods also contain shared networking and storage resources for their containers:

-   **Network:** Pods are automatically assigned unique IP addresses. Pod containers share the same network namespace, including IP address and network ports. Containers in a Pod communicate with each other inside the Pod on ```localhost```.

-   **Storage:** Pods can specify a set of shared storage volumes that can be shared among the containers.