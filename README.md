# AWS Airflow CI/CD

This repository contains a CI/CD pipeline for deploying Airflow DAGs using Docker and AWS S3.

## Introduction

This project aims to streamline the process of deploying Airflow DAGs by leveraging Docker containers and AWS S3 for storage. 
The continuous integration and continuous deployment (CI/CD) pipeline automates the deployment process, ensuring that changes to DAGs are quickly and reliably propagated to the Airflow environment.

## Setup

### Prerequisites

Before using this pipeline, ensure you have the following prerequisites installed:

- Docker
- AWS CLI

### Configuration

1. Clone this repository to your local machine.
2. Configure your AWS credentials using the `aws configure` command or by setting environment variables.
3. Customize the DAGs in the `dags` directory according to your requirements.

## Usage

### Running the CI/CD Pipeline

To deploy your DAGs using the CI/CD pipeline, follow these steps:

1. Make changes to your DAGs locally.
2. Commit and push your changes to the `main` branch of this repository.
3. The CI/CD pipeline will automatically trigger on each push to the `main` branch.
4. The pipeline will build a Docker image, run unit tests, deploy the DAGs to AWS S3, and trigger Airflow to reload the DAGs.

### Manual Deployment

If you prefer manual deployment, you can use the following commands:

- To build the Docker image: `docker build -t airflow-dags .`
- To run unit tests: `docker run airflow-dags python tests/test_dag.py`
- To deploy DAGs to S3: `aws s3 cp dags/ s3://airflowdockercicd/dags/ --recursive --delete`

## Folder Structure

- `dags`: Contains Airflow DAG files.
- `tests`: Contains unit and integration tests for the DAGs.
- `.github/workflows`: Contains GitHub Actions workflow files for CI/CD.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

