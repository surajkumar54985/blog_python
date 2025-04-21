import boto3
from app.core.config import settings

s3 = boto3.client(
    "s3",
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

def upload_to_s3(file_path, object_name):
    s3.upload_file(file_path, settings.AWS_BUCKET_NAME, object_name)
    return f"https://{settings.AWS_BUCKET_NAME}.s3.amazonaws.com/{object_name}"
