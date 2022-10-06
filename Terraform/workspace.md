## What is Terraform Workspace?

If we use the local backend for storing Terraform state, Terraform creates a file called *terraform.tfstate* to store the state of the applied configuration. However, in scenarios where you want to use the same configuration for different contexts, separate states might be necessary with same configuration.

Workspaces allows you to separate your state and infrastructure without changing anything in your code when you wanted the same exact code base to deploy to multiple environments without overlap. i.e. Workspaces help to create multiple state files for set of same terraform configuration files.

Each of environments required separate state files to avoid collision. With the use of workspaces, you can prepend the workspace name to the path of the state file, ensuring each workspace (environment) had its own state.

**Commands**

```bash
terraform workspace new Production
terraform workspace select Production
# Create deployment plan
terraform plan -out prod.tfplan
# Apply the deployment
terraform apply "prod.tfplan"
```

### Contributors
[![Yogendra Pratap Singh][yogendra_avatar]][yogendra_homepage]<br/>[Yogendra Pratap Singh][yogendra_homepage] 

  [yogendra_homepage]: https://www.linkedin.com/in/yogendra-pratap-singh-41630716b/
  [yogendra_avatar]: https://img.cloudposse.com/75x75/https://github.com/PratapSingh13.png