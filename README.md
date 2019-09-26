[![Build Status](https://travis-ci.org/104corp/cfn-basic-module.svg?branch=master)](https://travis-ci.org/104corp/cfn-basic-module)
[![NPM version](https://img.shields.io/npm/v/@104corp/cfn-basic-module.svg)](https://www.npmjs.com/package/@104corp/cfn-basic-module)

# cfn Basic module

* CloudTrail
* IAM Role
    * Role-Administrator (AdministratorAccess)
    * Role-Otter (AdministratorAccess)
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

## Parameters

