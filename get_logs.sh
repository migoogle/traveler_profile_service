#!/bin/bash

# This script fetches the logs for the traveler-profile-service Cloud Run service,
# and saves them to a file named logs.txt.

PROJECT_ID="emea-bootcamp-2025"
SERVICE_NAME="traveler-profile-service"
LOG_FILE="logs.txt"

echo "Fetching logs for service '$SERVICE_NAME' in project '$PROJECT_ID'வுகளை..."

gcloud logging read "resource.type=cloud_run_revision AND resource.labels.service_name=$SERVICE_NAME" \
    --project=$PROJECT_ID \
    --format="value(timestamp, textPayload)" > "$LOG_FILE"

echo "Logs saved to $LOG_FILE"