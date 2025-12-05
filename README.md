# Traveler Profile Service

This service provides a simple webhook to process traveler profile data. It's designed to be deployed as a Google Cloud Run service.

## How it Works

The service exposes a single endpoint: `/reinject_traveler_profile`.

This endpoint accepts `POST` requests with a JSON payload containing traveler profile information. It processes this data and returns a JSON object structured for display in an agent-facing UI.

### Data Transformation

The service performs the following transformations on the incoming data:
1.  It takes the input parameters from the request.
2.  It creates a JSON object with a key `agentDisplayMessage`.
3.  All values within the `agentDisplayMessage` object are converted to strings.
4.  Any `null` or `None` values are converted to a single space `" "`.

This ensures that the receiving application gets a consistent data structure with string-only values.

## Deployment to Google Cloud Run

Follow these steps to deploy the service to your own Google Cloud project.

### Prerequisites

*   Google Cloud SDK (`gcloud` CLI) installed and authenticated.
*   A Google Cloud Project with the Cloud Build and Cloud Run APIs enabled.

### Step 1: Build the Container Image

From the root directory of this project, run the following command to build the container image and push it to Google Container Registry (GCR):

```bash
gcloud builds submit --tag gcr.io/[PROJECT_ID]/[SERVICE_NAME]
```

Replace `[PROJECT_ID]` with your Google Cloud project ID and `[SERVICE_NAME]` with your desired service name (e.g., `traveler-profile-service`).

**Example:**
```bash
gcloud builds submit --tag gcr.io/emea-bootcamp-2025/traveler-profile-service
```

### Step 2: Deploy the Service

Once the image is built, deploy it to Cloud Run with the following command:

```bash
gcloud run deploy [SERVICE_NAME] --image gcr.io/[PROJECT_ID]/[SERVICE_NAME] --region [REGION] --platform managed --allow-unauthenticated
```

Replace the placeholders accordingly. The `--allow-unauthenticated` flag makes the service publicly accessible.

**Example:**
```bash
gcloud run deploy traveler-profile-service --image gcr.io/emea-bootcamp-2025/traveler-profile-service --region us-central1 --platform managed --allow-unauthenticated
```

After a successful deployment, the command will output the URL for your service.

## Logging

The service is configured to output logs to standard output. When running on Cloud Run, these logs are automatically sent to Google Cloud Logging.

A helper script, `get_logs.sh`, is provided to fetch and view the logs.

To use it, make sure it's executable and run it:
```bash
chmod +x get_logs.sh
./get_logs.sh
```
This will save the logs to a file named `logs.txt`. The application-specific logs are prefixed with `[APP]` for easy filtering.
