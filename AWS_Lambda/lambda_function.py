import json
import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

sns = boto3.client("sns")

TOPIC_ARN = "arn:aws:sns:ap-south-2:111222333444:EBS-EventAlert-Topic"


def lambda_handler(event, context):

    detail = event.get("detail", {})

    sns_event = detail.get("event", "Unknown")
    sns_time = event.get("time", "Unknown")
    sns_region = event.get("region", "Unknown")

    resources = event.get("resources", [])
    volume_id = resources[0].split("/")[-1] if resources else "Unknown"

    logger.info(
        json.dumps(
            {
                "event": sns_event,
                "volume_id": volume_id,
                "region": sns_region,
                "time": sns_time
            }
        )
    )

    sns_message = f"""
        Event: {sns_event}
        VolumeID: {volume_id}
        Region: {sns_region}
        Time: {sns_time}
        """

    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="EBS Notification",
        Message=sns_message
    )

    logger.info(
        json.dumps(
            {
                "message": "SNS notification published",
                "message_id": response["MessageId"]
            }
        )
    )

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "event": sns_event,
                "volume_id": volume_id,
                "sns_message_id": response["MessageId"]
            }
        )
    }
