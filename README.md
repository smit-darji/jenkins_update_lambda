# Jenkins → AWS Lambda CI/CD POC

This repository demonstrates a CI/CD pipeline using Jenkins to deploy updates to an AWS Lambda function automatically on push to the master branch.

## Flow
1. Developer pushes to master
2. GitHub triggers Jenkins webhook
3. Jenkins installs dependencies, packages Lambda
4. Jenkins updates Lambda via AWS Lambda Plugin

## Lambda Directory
All Lambda code lives inside:
    lambda_function/

Update handler.py and push to deploy.
