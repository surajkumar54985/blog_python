import boto3
import json
from app.core.config import settings
from fastapi import HTTPException

stepfunctions_client = boto3.client(
    'stepfunctions',
    region_name=settings.AWS_REGION,
    aws_access_key_id=settings.AWS_ACCESS_KEY,
    aws_secret_access_key=settings.AWS_SECRET_KEY
)

async def start_email_verification_step_function(email: str, token: str):
    try:
        input_payload = {"email": email, "token": token}
        response = stepfunctions_client.start_execution(
            stateMachineArn=settings.STEP_FUNCTION_ARN,
            input=json.dumps(input_payload)
        )
        return response
    except Exception as e:
        # Log this if you have a logger
        raise HTTPException(status_code=500, detail=f"Step Function execution failed: {str(e)}")
