from fastapi import APIRouter, UploadFile, File
from app.services.rekognition_service import detect_labels
from app.schemas.rekognition_schema import RekognitionResponse

router = APIRouter()

@router.post("/detect-labels", response_model=RekognitionResponse)
async def detect_image_labels(file: UploadFile = File(...)):
    return detect_labels(file)
