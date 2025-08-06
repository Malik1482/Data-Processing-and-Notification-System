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
