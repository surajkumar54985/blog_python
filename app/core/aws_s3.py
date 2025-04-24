import os
import boto3
from botocore.exceptions import NoCredentialsError
from fastapi import UploadFile
from uuid import uuid4
from app.core.config import settings

s3_client = boto3.client(
    's3',
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY,
    region_name=settings.AWS_REGION
)

def upload_file_to_s3(file: UploadFile, folder: str = "uploads"):
    file_extension = file.filename.split('.')[-1]
    unique_filename = f"{folder}/{uuid4().hex}.{file_extension}"

    
    try:
        s3_client.upload_fileobj(
            file.file,
            settings.AWS_BUCKET_NAME,
            unique_filename,
            ExtraArgs={"ContentType": file.content_type}
        )
        # file_url = f"https://{settings.AWS_BUCKET_NAME}.s3.{settings.AWS_REGION}.amazonaws.com/{unique_filename}"
        file_url = f"https://{settings.CLOUDFRONT_DOMAIN}/{unique_filename}"
        return file_url
    except NoCredentialsError:
        raise Exception("AWS credentials not found.")
