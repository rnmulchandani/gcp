#!/usr/bin/env python

# 1. pip install google-cloud-bigquery
# 2. set up your default credentials

import os
import uuid
from google.cloud import bigquery

#Comment this statement if you have already set default credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path-to-application-credentials-file"

# Parameters
PROJECT_ID = 'project-id'
DATA_SET = 'dataset-name'
TABLE_NAME = 'table-name'

client = bigquery.Client()

def get_gcp_daily_cost():
	QUERY = ("SELECT SUM(cost) AS cost FROM `"+ PROJECT_ID + "." + DATA_SET + "." + TABLE_NAME + "`" +
			"WHERE CAST(DATE(_PARTITIONTIME) AS DATE) = DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)")
	query_job = client.query(QUERY)
	rows = query_job.result()
	for row in rows:
		print("Daily Cost:", row.cost)

def get_gcp_monthly_cost():
	QUERY = ("SELECT SUM(cost) AS cost FROM `"+ PROJECT_ID + "." + DATA_SET + "." + TABLE_NAME + "`" +
			"WHERE _PARTITIONTIME >= TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), MONTH, 'UTC')"
			"AND _PARTITIONTIME < TIMESTAMP_TRUNC(CURRENT_TIMESTAMP(), DAY, 'UTC')")
	query_job = client.query(QUERY)
	rows = query_job.result()
	for row in rows:
		print("Monthly to Date Cost:", row.cost)

get_gcp_daily_cost()
get_gcp_monthly_cost()
