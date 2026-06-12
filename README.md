# Terraform EC2 GitHub Deployment

This project demonstrates how to use Terraform to create an AWS EC2 instance and automatically deploy a Python application from a GitHub repository.

## Technologies Used

- AWS EC2
- Terraform
- GitHub
- Linux
- Python

## Project Workflow

1. Terraform creates an EC2 instance in AWS.
2. User data script runs during instance startup.
3. The EC2 instance clones the Python application from GitHub.
4. The application is deployed automatically.

## Prerequisites

- AWS Account
- AWS CLI configured
- Terraform installed
- Git installed

## Usage

```bash
terraform init
terraform plan
terraform apply
```

## Learning Objectives

- Infrastructure as Code (IaC)
- AWS EC2 Provisioning
- Terraform Basics
- GitHub Integration
- Automated Deployment

## Author

Aajera
