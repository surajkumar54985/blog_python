import base64
from app.core.aws_rekognition import get_rekognition_client
from app.schemas.rekognition_schema import RekognitionResponse, Label
from fastapi import UploadFile

def detect_labels(file: UploadFile) -> RekognitionResponse:
    image_bytes = file.file.read()
    client = get_rekognition_client()
    response = client.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=70
    )
    labels = [Label(Name=label['Name'], Confidence=label['Confidence']) for label in response['Labels']]
    return RekognitionResponse(Labels=labels)
