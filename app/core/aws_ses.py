import boto3
from botocore.exceptions import BotoCoreError, ClientError
from app.core.config import settings

ses_client = boto3.client(
    'ses',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

def send_confirmation_email(email: str, token: str):
    try:
        confirmation_link = f"{settings.FRONTEND_BASE_URL}/confirm?token={token}"
        response = ses_client.send_email(
            Source=settings.SES_SENDER_EMAIL,
            Destination={"ToAddresses": [email]},
            Message={
                "Subject": {"Data": "Confirm your email"},
                "Body": {
                    "Text": {"Data": f"Click to confirm: {confirmation_link}"}
                }
            }
        )
        return response
    except (BotoCoreError, ClientError) as e:
        raise Exception(f"Email send failed: {str(e)}")
