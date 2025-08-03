# S214: Sales Data Processing and Notification System

<!-- Xgrid Learning and Development Program -->

## Overview

* The Sales Data Processing and Notification System is a serverless data processing and notification system implemented using AWS services. It processes sales data stored in an RDS database and sends a notification to users via email using Amazon SNS.

* The system is implemented using AWS Lambda, which is triggered on a daily schedule. The Lambda function fetches the RDS database credentials from AWS Secrets Manager, connects to the database, processes the sales data, and sends a notification to users via Amazon SNS.

* The system is deployed using AWS CloudFormation, which creates the necessary AWS resources and configures them based on the parameters specified by the user. The CloudFormation stack creates the RDS database instance, the SNS topic, and the Lambda function and their dependencies.

* The Sales Data Processing and Notification System is designed to be scalable, reliable, and cost-effective. It leverages AWS serverless services to minimize the infrastructure and maintenance costs, and it can be easily deployed and configured using AWS CloudFormation.

## Specialization Module Architecture 

![Architecture to follow](./diagram/infra.png)

### Tool & Technologies used:

You need to install the following tools:

 - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
 - [AWS IAM User Account](https://aws.amazon.com/console/)
 - [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

## Estimated Time To Complete:

1 sprint = 1 week

## Infrastructure as Code:

The Application's infrastructure will be provisioned using Cloudformation.

## Implementation

### List Of Resources

- VPC
  - Public Subnets
  - Private Subnets
  - Route Tables
  - Route Table Associations
  - Security Groups
- Internet Gateway
- NAT Gateway
- Elastic IP
- RDS (MySQL or PostgresSQL)
- Lambda Function(Inside VPC)
- SNS Topic
- Event Bridge Role
- Secrets Manager
- AWS System Manager(SSM) Parameters

### Deployment Instructions

- Please make sure to provision free-tier resources unless required or specified. Information on each service's types is available at the [aws website](https://aws.amazon.com/free/?all-free-tier).

- Make sure to de-provision infra. after you've given a demo or tested it. 

### Virtual Private Cloud  

The instructions for spinning up a fresh Virtual Private Cloud with its sub components using terraform is discussed in [VPC specialization module using terraform as infrastructure as code on AWS](https://github.com/X-CBG/xldp/tree/added-s206/cloud_specializations/s206),So you can refer it for a detailed walkthrough and sprint related guidelines of Specialization Module. And to create vpc and its related resources using cloudFormation you can follow this [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EC2.html).

### AWS Relational Database 

Now, you need to create an RDS with CloudFormation with engine of your choice ( MySQL OR PostgreSQL ). To create RDS using cloudformation look at this [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RDS.html)

### Secrets Manager

By using Secret Manager to store RDS credentials, you can improve the security and manageability of your applications, while reducing the overhead of managing secrets in-house. To Create a secret manager store look into this [link](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecretsManager.html).

### Lambda Function

Create a lambda function using cloudformation resources. And use AWS SDKs to get data from RDS database, process/refine it and send a notification using SNS. Lambda function should be able to put and get data from RDS. For putting the data in rds use lambda function as custom cloudformation resource. So that once lambda gets provisioned, it puts the data in RDS at once. After that use event bridge as second trigger to invoke lambda daily and send notifications using SNS. For lambda requirements follow these documentations.

1. [CloudFormation, AWS Lambda resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lambda.html)
2. [Lambda examples using SDK for Python](https://docs.aws.amazon.com/code-library/latest/ug/python_3_lambda_code_examples.html)
3. [AWS CloudFormation CustomResource Lambda Function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html)
4. [connect MySQL Database to AWS LAMBDA](https://medium.com/@himanshu_88759/how-to-connect-mysql-database-to-aws-lambda-using-python-485e7fdfae56)
5. [What is the AWS Serverless Application Model (AWS SAM)?](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
6. [Invoking Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html)

**Tip**: Connection b/w AWS lambda & RDS needs python libraries(Not in lambda be default). These libraries can be used through lambda layers or AWS SAM cli.

### SNS Topic

 An SNS topic is being used to send notifications to users. Once the Lambda function has processed the data from the RDS database, it sends a notification to an SNS topic. The SNS topic then sends the notification to the subscribed users via email.

 1. [Amazon Simple Notification Service resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SNS.html)
 2. [SNS SDKs to be used in AWS lambda](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html)

### Event Bridge

AWS event bridge is used to trigger lambda function on the basis of specific events. The choice of Lambda invoke schedule depends on the specific needs of your project. In this project, the Lambda function is invoked on a daily basis using EventBridge. However, it is possible to configure the Lambda function to be invoked on a different schedule, depending on your requirements.
Here are some common Lambda invoke schedules and their benefits:
* **Daily:** A daily schedule is suitable for tasks that need to be performed on a regular basis, such as processing sales data or generating reports. This schedule provides a good balance between automation and frequency, allowing you to automate tasks without overwhelming your resources.
* **Weekly:**  A weekly schedule is suitable for tasks that don't need to be performed as frequently, such as data backups or weekly reports. This schedule can help reduce the number of executions and associated costs, while still providing regular automation.
* **Monthly:** A monthly schedule is suitable for tasks that only need to be performed once a month, such as generating monthly invoices or performing end-of-month processing. This schedule provides the lowest level of automation but can be useful for infrequent or low-priority tasks.

To create a Event Bridge role using lambda look at the link [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Events.html)

### SSM Parameter Store

SSM Parameters allow you to store and manage configuration data in a centralized location, which makes it easier to manage and update this data across multiple environments and applications. This can be used to reference output parameters from one template to another template.

1. [AWS Systems Manager resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-parameter.html).
2. [Using dynamic references to specify template values](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html)

## BONUS / Level Up

Use AWS Simple Email Service(SES) to send a pdf report or a table using HTML rendering to the user as a notification email.

1. [Amazon Simple Email Service resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SES.html)
2. [Sending Emails with SES and Lambda](https://www.thelambdablog.com/sending-email-with-aws-ses-and-a-python-lambda-using-cloudformation/)

## Deliverables

### CloudFormation Templates: 

Acceptance criteria includes Cloudformation or sam templates with all the modules deploying successfully.

**Note:** _Create Different templates for Major resources like Separate template for VPC,RDS and Lambda etc. And use SSM parameter Store to use the required parameters._

### Results 

You need to attach the expected results of the sprint outcome like screenshot of your lambda logs and sns emails of the data you received.

### Documentation:

Write a markdown README doc defining the architecture of your application and commit it to a GitHub repo.
