[![Build Status](https://travis-ci.com/104corp/cfn-basic-module.svg?branch=master)](https://travis-ci.com/104corp/104isgd-devops-cfn-basic.svg?token=XzF5xSuVcyG4W3apP4Dr&branch=master)
[![NPM version](https://img.shields.io/npm/v/@104corp/cfn-basic-module.svg)](https://www.npmjs.com/package/@104corp/cfn-basic-module)

# cfn Basic module

* CloudTrail
* IAM Role for administrator 
    * Role-Administrator (AdministratorAccess)
* AWS Config
* AWS Health Event notify owner (slack)


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
  Bucket:
    Type: 'AWS::CloudFormation::Stack'
    Properties:
      Parameters:
        SlackWebhookURL: '' # optional
        CloudTrailS3BucketName: '' # optional
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

