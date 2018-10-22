# Google Cloud Platform Billing Utility

## 1. Introduction

Tools for monitoring, analyzing and optimizing cost have become an important part of managing development. The purpose of this script is to provide daily and month to date cost of resources utilized on GCP.

## 2. Pre-requisites
1. Enable [Export Billing Data to BigQuery](https://cloud.google.com/billing/docs/how-to/export-data-bigquery)
2. Install Python
3. Install google-cloud-bigquery module

## 3. Use
Before running this script, you need to modify some parameters:

- Set GOOGLE\_APPLICATION_CREDENTIALS environment variable **Or** Provide path to Google application credentials file  
- Set PROJECT\_ID, DATA\_SET , TABLE\_NAME variables
- Run using following command  
  `python gcp_billing.py`

Note: If you are providing GOOGLE\_APPLICATION_CREDENTIALS as an environment variable to the script then comment the line number 11 of script.