import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def get_rekognition_client():
    return boto3.client(
        'rekognition',
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY")
    )
