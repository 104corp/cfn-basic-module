# CloudFormation Basic module

[![Build Status](https://travis-ci.com/104corp/cfn-basic-module.svg?branch=master)](https://travis-ci.com/104corp/104isgd-devops-cfn-basic.svg?token=XzF5xSuVcyG4W3apP4Dr&branch=master)
[![NPM version](https://img.shields.io/npm/v/@104corp/cfn-basic-module.svg)](https://www.npmjs.com/package/@104corp/cfn-basic-module)

* CloudTrail
* IAM Role for administrator 
    * Role-Administrator (AdministratorAccess)
* AWS Health Event notify owner (slack)
* AWS Config
* AWS Config Rule
    * For Security
        * AWS CLOUD_TRAIL_ENABLED
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

### SlackWebhookURL 
Type: String 
Default: None 
Description: (Optional) send notify to slack webhook url 
### CloudTrailS3BucketName 
Type: String  
Description: (Optional) If you already have a cloudtrail s3 bucket 
### EnableConfigService 
Type: String  
Description: (Optional) enable config service or not 
### ConfigS3BucketName 
Type: String  
Description: (Optional) If you already have a aws config s3 bucket 
### AdminAccountId 
Type: String  
Description: (Optional) AWS Account Id of the administrator account for assume role 

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
### AWSServiceRoleForConfig 
Type: AWS::IAM::ServiceLinkedRole  
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

## Outputs
The list of outputs this template exposes:

## Maintenance

Maintainers:
  - `104corp`