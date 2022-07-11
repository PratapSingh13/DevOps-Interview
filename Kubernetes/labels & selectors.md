- **What are labels?**
Labels are the mechanism used to organize Kubernetes objects. A label is a key-value pair with certain restrictions concerning length and allowed values but without any pre-defined meaning. You're free to choose labels as you see fit.

- **Why do we need labels?**
If we talk about the kubernetes cluster, there are various components in k8s cluster even a small Kubernetes cluster may have hundreds of Containers, Pods, Services and many other Kubernetes API objects. So quickly it becomes annoying to find out  various objects inside the cluster. 

So suppose I need to create a replicatio-controller on the basis of those pods which are type of *backend* and name is **myapp** only. So for this we need to set labels in deployment with the label of *type: backend* and *name: myapp*. So when replication-controller found any pod with given label it will work what it should.

**The primary reasons you should use labels are:**
- It enables you to logically organize all your Kubernetes workloads in all your clusters.
- Enables you to very selectively filter kubectl outputs to just the objects you need.

*Syntax of labels in k8s manifest*

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: label-demo
  labels:
    environment: production
    app: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.14.2
    ports:
    - containerPort: 80
```


*Check how to see labels on a pod*

```kubectl get pods --show-labels```


*You can add a label to the pod through the *label* subcommand:*

```kubectl label pods <pod-name> type=backend```

*To list all the pods with **type: backend***

```kubectl get pods -l type=backend```

*To add label on a running pod*

```kubectl label pods <pod-name> <labelKey: labelValue>```

*To overwrite a label of a running pod*

```kubectl label pods <pod-name>  labelKey=labelValue> --overwrite```

*To delete a label from a running pod*

```kubectl label pods <pod-name>  <labelKey->```
