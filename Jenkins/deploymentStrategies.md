# Application Deployment Strategies
-   Recreate
-   Rolling Update(Ramped)
-   Blue/Green
-   Canary


### **Recreate**

The recreate strategy is a dummy deployment which  shutting down version A first then deploy version B after version A is turned off.

This technique takes downtime of the service that depends on both shutdown and boot duration of the application.

**Pros**

-   Easy to setup
-   Application state entirely renewed.

**Cons**

-   High impact on the user, expect downtime that depends on both shutdown and boot duration of the application.


### **Rolling Update**

Rolling Update strategy consists of slowly rolling out a version of an application by replacing instances one after the other until all the instances are rolled out. It usually follows like with a pool of version A behind a load balancer, one instance of version B is deployed. When the service is ready to accept traffic, the instance is added to the pool. Then, one instance of version A is removed from the pool and shut down.

We can tweak the parameters to increase the deployment time:

-   **Max batch size:** Number of concurrent instances to roll out.

-   **Max surge:** How many instances to add in addition of the current amount. For example, when the value is set to 30%, the new ReplicaSet will be scaled up immediately when the rolling update starts, so that the total number of old and new Pods does not exceed 130% of desired Pods. Once old Pods have been killed, the new ReplicaSet can be scaled up further, ensuring that the total number of Pods running at any time during the update is at most 130% of desired Pods.

-   **Max unavailable:** Number of unavailable instances during the rolling update procedure. For example, when the value is set to 30%, the old ReplicaSet can be scaled down to 70% of desired Pods immediately when the rolling update starts. Once new Pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of Pods available at all times during the update is at least 70% of the desired Pods.

**Pros**
-   Easy to set up.
-   Version is slowly released across instances.
-   Convenient for stateful applications that can handle rebalancing of the data.

**Cons**
-   Rollout/rollback can take time.
-   No control over traffic.

### **Blue/Green**
In blue/green deployment strategy  version B (green) is deployed alongside version A (blue) with exactly the same amount of instances. After testing the new version if it meets all the requirements, then the traffic is switched from version A to version B at the load balancer level.

**Pros**
-   Instant rollout/rollback.
-   Avoid versioning issue, the entire application state is changed in one go.

**Cons**
-   Expensive as it requires double the resources.
-   Proper test of the entire platform should be done before releasing to production.
-   Handling stateful applications can be hard.

### **Canary**
A canary deployment consists of gradually shifting production traffic from version A to version B. Usually the traffic is split based on weight. For example, 90 percent of the requests go to version A, 10 percent go to version B.

This technique is mostly used when the tests are lacking or not reliable or if there is little confidence about the stability of the new release on the platform.

**Pros**
-   Version released for a subset of users.
-   Convenient for error rate and performance monitoring.
-   Fast rollback.

**Cons**
-   Slow rollout

Click here for more information on [Deployment Strategies][deploymentStrategiesLink]

[deploymentStrategiesLink]: https://thenewstack.io/deployment-strategies/



### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://github.com/PratapSingh13
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png