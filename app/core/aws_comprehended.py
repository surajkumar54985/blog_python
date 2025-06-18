import boto3
from app.core.config import settings

def get_comprehend_client():
    return boto3.client(
        'comprehend',
        region_name=settings.AWS_REGION,
        aws_access_key_id=settings.AWS_ACCESS_KEY,
        aws_secret_access_key=settings.AWS_SECRET_KEY
    )
