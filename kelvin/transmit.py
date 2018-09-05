import boto3


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




