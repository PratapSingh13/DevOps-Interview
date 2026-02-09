# Init Containers

The init containers option is available in Kubernetes environments used to run additional containers at startup that help initialize an application. Once the init containers have completed their initialization tasks, they terminate but leave the application container(s) running.

### Overview on Kubernetes init containers

- An init container is an additional container in a Pod **that completes a task before the regular container is started.**
- We can have multiple init containers in a Pod 
- Each init container must complete successfully before the next one starts.
- The regular container will only be started once the init container has been completed.
- This is a great way to initialize a Kubernetes pod. You can pull any files, configurations, and so on with an init container.

### Differences from regular containers
- Init containers support all the fields and features of app containers, including resource limits, volumes, and security settings.
- init containers do not support lifecycle, livenessProbe, readinessProbe, or startupProbe because they must run to completion before the Pod can be ready.
- If you specify multiple init containers for a Pod, kubelet runs each init container sequentially. Each init container must succeed before the next can run. When all of the init containers have run to completion, kubelet initializes the application containers for the Pod and runs them as usual.

#### Create a Pod with initContainers

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myfirstpod
  labels:
  label1: harshal
  label2: gaurav
  label3: saurav
spec:
  containers:
    - name: firstcontainer
      image: pratapsingh13/nginx-custom
      env:
        - name: myname
          value: yogendra
        - name: city
          value: Kanpur
  initContainers:
    - name: initcontainer
      image: pratapsingh13/nginx-custom
      args: ["sleep", "30"]
```



---

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png