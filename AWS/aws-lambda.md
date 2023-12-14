- **Introduction to AWS Lambda**

  AWS Lambda is a compute service that run your code without provisioning or managing servers that is why AWS Lambda also known as serverless computing.

  With AWS Lambda you can run code for virtually any type of application or backend service - ALL WITH ZERO ADMINISTRATION. (ZERO ADMINISTRATION means we don't need to think about how Lambda is working, How Lambda maintenance is going on these all taken by AWS itself).

  - AWS Lambda manages all the administration itself - 

    1. Provisioning and capacity of compute fleet that offers balance of memory, CPU, network and other resources.
    2. Server and OS maintenance.
    3. High availability and automatic scaling.
    4. Maintaining fleet health.
    5. Applying security patches.
    6. Monitoring and logging for Lambda function.

  AWS Lambda executes your code only when needed and scales automatically, from a few request per day to thousands per seconds (For this we basically setup event to trigger lambda function for certian situation automatically).

  You pay only for compute time you consume. No charge when your lambda function is not running.

  Integration with other AWS services: AWS Lambda integrates seamlessly with a wide range of AWS services, including Amazon S3, Amazon Kinesis, and Amazon DynamoDB. This makes it easy to build serverless applications that leverage the full range of AWS capabilities.

- **How Lambda function works ?**
  
  First you upload your code on lambda function it could be either one or more function.

  AWS Lambda will executes your code on your behalf in a certain event only.

  After the code is invoked, Lambda automatically take care of provisioning and managing the required resources.

**Note-:** *We can trigger a lambda function from another lambda function.*

  