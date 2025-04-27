import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("Received event: %s", json.dumps(event, indent=2))


    for record in event.get('Records', []):
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        logger.info(f"New object created in bucket: {bucket_name}, Object key: {object_key}")

    return {
        'statusCode': 200,
        'body': json.dumps('S3 Event logged successfully!')
    }
