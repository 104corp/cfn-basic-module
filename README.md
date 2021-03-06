# CloudFormation Basic module

[![Build Status](https://travis-ci.com/104corp/cfn-basic-module.svg?branch=master)](https://travis-ci.com/104corp/104isgd-devops-cfn-basic.svg?token=XzF5xSuVcyG4W3apP4Dr&branch=master)
[![NPM version](https://img.shields.io/npm/v/@104corp/cfn-basic-module.svg)](https://www.npmjs.com/package/@104corp/cfn-basic-module)

* CloudTrail
* IAM Role for administrator 
    * Role-Administrator (AdministratorAccess)
* AWS Health Event notify owner (slack)
* AWS Config
* AWS Config Rule
    * For Monitor
        * AWS ACM_CERTIFICATE_EXPIRATION_CHECK
    * For Security
        * AWS CLOUD_TRAIL_ENABLED
        * IAM_ROOT_ACCESS_KEY_CHECK
        * ROOT_ACCOUNT_MFA_ENABLED
        * RDS_INSTANCE_PUBLIC_ACCESS_CHECK
        * ELB_LOGGING_ENABLED
        * VPC_FLOW_LOGS_ENABLED
        * DYNAMODB_TABLE_ENCRYPTION_ENABLED
    * For Cost
        * AWS EIP_ATTACHED
        * AWS EC2_VOLUME_INUSE_CHECK


## Install

> Install [Node.js and npm](https://nodejs.org/) first!

```
npm i @104corp/cfn-basic-module
```

## Usage

```
---
AWSTemplateFormatVersion: '2010-09-09'
Description: 'cfn-basic-module example'
Resources:
  Basic:
    Type: 'AWS::CloudFormation::Stack'
    Properties:
      Parameters:
        SlackWebhookURL: '' # optional
        CloudTrailS3BucketName: '' # optional
        EnableConfigService: '' # optional
        ConfigS3BucketName: '' # optional  
        AdminAccountId: '' # optional
      TemplateURL: './node_modules/@104corp/cfn-basic-module/module.yml'
```

## Package

```
$ aws cloudformation package --template-file example.yml --s3-bucket <your cfn template bucket> --output-template-file packaged.yml
```

## Deploy

```
$ aws cloudformation deploy --template-file packaged.yml --stack-name <your stack name>
```

## Parameters

# templates/module
# Description
A basic template

## Parameters
The list of parameters for this template:

### MainRegion 
Type: String 
Default: None 
Description: (Optional) create in main region 
### SlackWebhookURL 
Type: String 
Default: None 
Description: (Optional) send notify to slack webhook url 
### AdminPrincipal 
Type: String 
Default: None 
Description: (Optional) AWS Account Principal of the administrator account for assume role 
### EnableCloudTrail 
Type: String  
Description: (Optional) enable CloudTrail or not 
### CloudTrailS3BucketName 
Type: String 
Default: None 
Description: (Optional) If you already have a cloudtrail s3 bucket 
### EnableConfigService 
Type: String  
Description: (Optional) enable config service or not 
### ConfigS3BucketName 
Type: String 
Default: None 
Description: (Optional) If you already have a aws config s3 bucket 
### ConfigSNSTopicArn 
Type: String 
Default: None 
Description: (Optional) config sns topic arn. 
### CofingRulePrefix 
Type: String 
Default: None 
Description: (Optional) config rule name prefix 
### ACMCertificatesDaysToExpiration 
Type: Number  
Description: (Optional) Checks whether ACM Certificates in your account are marked for expiration within the specified number of days. 
### EnableEIPAttachedConfigRule 
Type: String  
Description: (Optional) enable Checks whether all EIP addresses allocated to a VPC are attached to EC2 instances or in-use ENIs. 
### EnableEC2VolumeInuseCheckConfigRule 
Type: String  
Description: (Optional) enable Checks whether EBS volumes are attached to EC2 instances. 
### EnableIAMRootKeyCheckConfigRule 
Type: String  
Description: (Optional) enable Checks whether the root user access key is available. 
### EnableRootMFAEnabledConfigRule 
Type: String  
Description: (Optional) enable Checks whether the root user of your AWS account requires multi-factor authentication for console sign-in. 
### EnableRDSPublicAccessCheckConfigRule 
Type: String  
Description: (Optional) enable Checks whether the Amazon Relational Database Service (RDS) instances are not publicly accessible. The rule is non-compliant if the publiclyAccessible field is true in the instance configuration item. 
### EnableSGOpenOnlyToAuthorizedPortsConfigRule 
Type: String  
Description: (Optional) enable Checks whether any security groups with inbound 0.0.0.0/0 have TCP or UDP ports accessible. The rule is NON_COMPLIANT when a security group with inbound 0.0.0.0/0 has a port accessible which is not specified in the rule parameters. 
### SGOpenAuthorizedTcpPorts 
Type: String 
Default: 80,443 
Description: (Optional) Comma-separated list of TCP ports authorized to be open to 0.0.0.0/0. Ranges are defined by a dash; for example, "443,1020-1025". 
### SGOpenAuthorizedUdpPorts 
Type: String 
Default: 0 
Description: (Optional) Comma-separated list of UDP ports authorized to be open to 0.0.0.0/0. Ranges are defined by a dash; for example, "500,1020-1025". 
### EnableVPCFlowLogsEnabledConfigRule 
Type: String  
Description: (Optional) enable Checks whether Amazon Virtual Private Cloud flow logs are found and enabled for Amazon VPC. 
### VPCFlowLogTrafficType 
Type: String 
Default: None 
Description: (Optional) vpc flow log traffic type 
### EnableELBLoggingEnabledConfigRule 
Type: String  
Description: (Optional) enable Checks whether the Application Load Balancers and the Classic Load Balancers have logging enabled. 
### ELBLoggingS3BucketNames 
Type: String 
Default: None 
Description: (Optional) elb logging s3 bucket name 
### EnableDynamodbEncryptionConfigRule 
Type: String  
Description: (Optional) enable Checks whether the Amazon DynamoDB tables are encrypted and checks their status. The rule is compliant if the status is enabled or enabling. 

## Resources
The list of resources this template creates:

### EventRule 
Type: AWS::Events::Rule  
### PermissionForEventsToInvokeLambda 
Type: AWS::Lambda::Permission  
### LambdaExecutionRole 
Type: AWS::IAM::Role  
### LambdaFunction 
Type: AWS::Lambda::Function  
### CloudTrailS3Bucket 
Type: AWS::S3::Bucket  
### CloudTrailS3BucketPolicy 
Type: AWS::S3::BucketPolicy  
### CloudTrail 
Type: AWS::CloudTrail::Trail  
### CloudTrailWithS3 
Type: AWS::CloudTrail::Trail  
### AdministratorRole 
Type: AWS::IAM::Role  
### ConfigS3Bucket 
Type: AWS::S3::Bucket  
### ConfigS3BucketPolicy 
Type: AWS::S3::BucketPolicy  
### RoleForConfig 
Type: AWS::IAM::Role  
### ConfigRecorder 
Type: AWS::Config::ConfigurationRecorder  
### ConfigDeliveryChannel 
Type: AWS::Config::DeliveryChannel  
### ConfigDeliveryChannelWithS3 
Type: AWS::Config::DeliveryChannel  
### CloudTrailEnabledConfigRule 
Type: AWS::Config::ConfigRule  
### EIPAttachedConfigRule 
Type: AWS::Config::ConfigRule  
### EC2VolumeInuseCheckConfigRule 
Type: AWS::Config::ConfigRule  
### ACMExpirationCheckConfigRule 
Type: AWS::Config::ConfigRule  
### IAMRootKeyCheckConfigRule 
Type: AWS::Config::ConfigRule  
### RootMFAEnabledConfigRule 
Type: AWS::Config::ConfigRule  
### RDSPublicAccessCheckConfigRule 
Type: AWS::Config::ConfigRule  
### SGOpenOnlyToAuthorizedPortsConfigRule 
Type: AWS::Config::ConfigRule  
### VPCFlowLogsEnabledConfigRule 
Type: AWS::Config::ConfigRule  
### ELBLoggingEnabledConfigRule 
Type: AWS::Config::ConfigRule  
### DynamodbEncryptionConfigRule 
Type: AWS::Config::ConfigRule  

## Outputs
The list of outputs this template exposes:

## Maintenance

Maintainers:
  - `104corp`