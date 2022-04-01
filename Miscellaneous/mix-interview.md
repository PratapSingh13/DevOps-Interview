- What is Continuous Integration?

  Continuous Integration is the automation of builds. Depending on your source control/version control strategy, code changes for a bug fix or new feature need to be merged/committed into a branch in the source code repository. No matter which side of the mono-repo vs. multi-repo argument you are on, a build – and eventually, release artifacts – will be created as part of the Continuous Integration processes. 
![](/DevOps-Interview/images/CI.png)

- What is Continuous Delivery?

  Continuous delivery (CD) picks up where CI leaves off. It focuses on the later stages of a pipeline, where a completed build is thoroughly tested, validated and delivered for deployment. Continuous delivery can -- but does not necessarily -- deploy a successfully tested and validated build. 

- What is Continuous Deployment?

  Continuous deployment is a strategy in software development where code changes to an application are released automatically into the production environment. This automation is driven by a series of predefined tests. Once new updates pass those tests, the system pushes the updates directly to the software's users.

- What is difference between Continuous Delivery and Continuous Deployment?

  While “continuous deployment” and “continuous delivery” may sound like the same thing, they are actually two different approaches to frequent release.

  Continuous delivery is a software development practice where software is built in such a way that it can be released into production at any given time. To accomplish this, a continuous delivery model involves production-like test environments. New builds performed in a continuous delivery solution are automatically deployed into an automatic quality-assurance testing environment that tests for any number of errors and inconsistencies. After the code passes all tests, continuous delivery requires human intervention to approve deployments into production. The deployment itself is then performed by automation.

  Continuous deployment takes automation a step further and removes the need for manual intervention. The tests and developers are considered trustworthy enough that an approval for production release is not required. If the tests pass, the new code is considered to be approved, and the deployment to production just happens.



![](/DevOps-Interview/images/CI%3ACD.png)
