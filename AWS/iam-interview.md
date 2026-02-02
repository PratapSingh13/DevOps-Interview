**An IAM user has two attached IAM policies: one explicitly "Allows" access to an S3 bucket, and the other explicitly "Denies" the same action. What will happen if the user tries to access the bucket?**

**Answer-** Access will be denied because "Deny" takes precedence over "Allow".

**A company needs to share access to DynamoDB in your account with an external consultant. What is the best approach?**

**Answer-** Use a cross-account IAM role with a trust policy.
