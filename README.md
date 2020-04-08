# Simple Data Pipeline

## Objective
We want to create a simple data pipeline.

## Step 1 (Source)
Since I have a twitter account I decided to use the developer tools to get access to the API. Unfortunately I am limited to a 100 requests an hour, so that will have to do for now.

TwitterApi.py

## Step 2 (Storage)

The output of TwitterApi.py is saved to a json file.
We can now store this JSON file in S3.

TwitterApi_v1.1.py

#### Ingestion
