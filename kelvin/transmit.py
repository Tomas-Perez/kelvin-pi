import boto3
from botocore.exceptions import EndpointConnectionError
import json


class SQSTransmit:
    """
    Wrapper over boto3 client to help with report sending
    """
    def __init__(self, url):
        self.sqs = boto3.client('sqs')
        self.url = url

    def send_message(self, msg):
        """
        Send a string message
        :param msg: message to send
        :return: SQS response
        """
        response = None
        try:
            response = self.sqs.send_message(
                QueueUrl=self.url,
                DelaySeconds=10,
                MessageBody=msg
            )
        except EndpointConnectionError:
            pass
        return response

    def send_dict_as_json(self, a_dict):
        """
        Parse a dict to json and send as string
        :param a_dict: dict to send
        :return: SQS Response
        """
        return self.send_message(json.dumps(a_dict))
