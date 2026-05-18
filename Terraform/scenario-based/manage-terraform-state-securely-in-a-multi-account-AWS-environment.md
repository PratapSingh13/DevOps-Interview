# How do you manage Terraform state securely in a multi-account AWS environment?

In a multi-account AWS environment, Terraform state management should be designed with strong isolation, security, scalability, and governance controls because the state file contains sensitive infrastructure metadata and sometimes secrets.

**Each account should ideally have:**

* Separate Terraform backend
* Separate IAM roles
* Separate CI/CD access controls

This reduces blast radius and improves security boundaries.

## Use Remote Backend with S3 + DynamoDB

We store Terraform state remotely in Amazon S3 and use DynamoDB for state locking.

```HCL
terraform {
  backend "s3" {
    bucket         = "prod-terraform-state-bucket"
    key            = "network/vpc/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-state-lock"
    encrypt        = true
  }
}
```

## Enable S3 Security Controls

**For the state bucket:**

* Enable versioning
* Enable server-side encryption
* Block all public access
* Use bucket policies with least privilege
* Enable access logging if required

## Use DynamoDB for State Locking

DynamoDB prevents concurrent Terraform operations.

**Without locking:**

* Two engineers/pipelines can corrupt state simultaneously.

**With locking:**

* Terraform acquires lock before apply
* Other operations wait/fail safely

## Use Cross-Account IAM Roles

**Instead of static AWS credentials:**

* CI/CD pipeline assumes IAM role in target account
* Use STS AssumeRole
* Temporary credentials only

## Separate State Per Infrastructure Layer

We never keep all infrastructure in one state file.

**Example segregation:**

* Networking state
* IAM state
* ECS/EKS state
* Database state
* Monitoring state

**Benefits:**

* Reduced blast radius
* Faster plan/apply
* Easier team ownership
* Reduced lock contention

## Restrict Direct Human Access

**Best practice:**

* Developers should not directly modify production state
* Only CI/CD pipelines or privileged DevOps roles should access backend

## Handle Sensitive Data Carefully

**Terraform state can contain:**

* Passwords
* Endpoints
* Tokens
* Secrets

**So we:**

* Avoid hardcoding secrets
* Use AWS Secrets Manager/SSM
* Mark outputs as sensitive
* Encrypt backend using KMS

## Disaster Recovery Strategy

**We enable:**

* S3 versioning
* Cross-region replication
* State backup policies