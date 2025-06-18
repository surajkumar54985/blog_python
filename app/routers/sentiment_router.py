from fastapi import APIRouter
from app.schemas.sentiment import SentimentRequest, SentimentResponse
from app.services.comprehend_service import analyze_sentiment

router = APIRouter()

@router.post("/", response_model=SentimentResponse)
def get_sentiment(request: SentimentRequest):
    return analyze_sentiment(request)
