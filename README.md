# AWS MWAA Airflow CI/CD Pipeline

This repository contains a CI/CD pipeline for deploying Airflow DAGs on AWS Managed Workflows for Apache Airflow (MWAA) using GitHub Actions and AWS S3.

## Introduction

The CI/CD pipeline automates the deployment process, ensuring that changes to DAGs are quickly and reliably propagated to the Airflow environment on AWS MWAA.

## Features

- Continuous Integration: Automatically runs unit tests whenever changes are pushed to the repository to ensure code quality.
- Continuous Deployment: Automates the deployment process, pushing updated DAGs and requirements files to AWS S3 for Airflow to consume.
- Integration with AWS MWAA: Seamlessly integrates with AWS Managed Workflows for Apache Airflow, allowing for efficient management and execution of DAGs.
- GitHub Actions: Utilizes GitHub Actions for orchestrating the CI/CD pipeline, providing a flexible and configurable automation framework.

## Setup

### Prerequisites

Before using this pipeline, ensure you have the following prerequisites installed:

- Access to an AWS MWAA environment
- GitHub repository with your Airflow DAGs
- AWS CLI configured with appropriate permissions

### Configuration

1. Clone this repository to your local machine.
2. Customize the DAGs in the `dags` directory according to your requirements.
3. Set up your AWS credentials and region in your GitHub repository secrets.

## Usage

### Running the CI/CD Pipeline

To deploy your DAGs using the CI/CD pipeline, follow these steps:

1. Make changes to your DAGs locally.
2. Commit and push your changes to the `main` branch of this repository.
3. The CI/CD pipeline will automatically trigger on each push to the `main` branch.
4. The pipeline will build a Docker image, run unit tests, deploy the DAGs to AWS S3, and trigger Airflow to reload the DAGs.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

