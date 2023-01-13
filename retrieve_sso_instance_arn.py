import boto3
import logging
import botocore

# Setup Boto3 Clients
sso_client = boto3.client("sso-admin")

# Setup Logger
logging.basicConfig(
    format="%(asctime)s  %(levelname)s %(filename)s at lineno  %(lineno)d %(message)s"
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
        try:
            response = sso_client.list_instances()
            SSOId = response["Instances"][0]["InstanceArn"]
        except botocore.exceptions.ClientError as error:
            logger.error(error)
            raise error

        return  SSOId
