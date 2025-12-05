# Google Cloud Run Command Reference

This document provides a reference for the `gcloud` commands used to manage the AI Coach Workflow Engine on Google Cloud Run.

## Building the Container Image

To build the container image and push it to the Google Container Registry (GCR), use the following command:

```bash
gcloud builds submit --tag gcr.io/[PROJECT_ID]/[SERVICE_NAME]
```

*   `[PROJECT_ID]`: Your Google Cloud project ID.
*   `[SERVICE_NAME]`: The name of your service.

**Example:**

```bash
gcloud builds submit --tag gcr.io/emea-bootcamp-2025/workflow-engine
```

This command builds a Docker image from the `Dockerfile` in the current directory, tags it with the specified name, and pushes it to GCR.

## Deploying the Service

To deploy the container image to Cloud Run, use the following command:

```bash
gcloud run deploy [SERVICE_NAME] --image gcr.io/[PROJECT_ID]/[SERVICE_NAME] --region [REGION] --platform managed --allow-unauthenticated
```

*   `[SERVICE_NAME]`: The name of your service.
*   `[PROJECT_ID]`: Your Google Cloud project ID.
*   `[REGION]`: The region where you want to deploy your service.

**Example:**

```bash
gcloud run deploy workflow-engine --image gcr.io/emea-bootcamp-2025/workflow-engine --region us-central1 --platform managed --allow-unauthenticated
```

This command deploys the specified container image to the `workflow-engine` service in the `us-central1` region. The `--platform managed` flag specifies that you are using the fully managed version of Cloud Run, and the `--allow-unauthenticated` flag allows public access to the service.

## Viewing Logs

To view the logs for a Cloud Run service, use the following command:

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=[SERVICE_NAME]" --project=[PROJECT_ID]
```

*   `[SERVICE_NAME]`: The name of your service.
*   `[PROJECT_ID]`: Your Google Cloud project ID.

**Example:**

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=workflow-engine" --project=emea-bootcamp-2025
```

This command retrieves the logs for the `workflow-engine` service.

## Saving Logs to a File

To save the logs to a file, you can redirect the output of the `gcloud logging read` command:

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=[SERVICE_NAME]" --project=[PROJECT_ID] --format=json > [FILENAME]
```

*   `[SERVICE_NAME]`: The name of your service.
*   `[PROJECT_ID]`: Your Google Cloud project ID.
*   `[FILENAME]`: The name of the file to save the logs to.

**Example:**

```bash
gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=workflow-engine" --project=emea-bootcamp-2025 --format=json > logs.json
```

This command retrieves the logs for the `workflow-engine` service in JSON format and saves them to a file named `logs.json`.
