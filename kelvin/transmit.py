import boto3
import json


class SQSTransmit:
    def __init__(self, url):
        self.sqs = boto3.client('sqs')
        self.url = url

    def send_message(self, msg):
        response = self.sqs.send_message(
            QueueUrl=self.url,
            DelaySeconds=10,
            MessageBody=msg
        )
        return response

    def send_dict_as_json(self, a_dict):
        return self.send_message(json.dumps(a_dict))
