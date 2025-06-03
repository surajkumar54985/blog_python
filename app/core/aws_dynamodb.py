import boto3
from datetime import datetime
from app.core.config import settings

# Initialize DynamoDB resource
dynamodb = boto3.resource(
    'dynamodb',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

# Reference your table
table = dynamodb.Table("EmailConfirmations")

def log_email_confirmation(email: str, token: str):
    try:
        response = table.put_item(
            Item={
                "email": email,
                "timestamp": datetime.utcnow().isoformat(),
                "token": token,
                "status": "confirmed"
            }
        )
        return response
    except Exception as e:
        print(f"Error logging to DynamoDB: {str(e)}")
        return None
