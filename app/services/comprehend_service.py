from app.core.aws_comprehended import get_comprehend_client
from app.schemas.sentiment import SentimentRequest, SentimentResponse

def analyze_sentiment(request: SentimentRequest) -> SentimentResponse:
    client = get_comprehend_client()
    
    response = client.detect_sentiment(
        Text=request.text,
        LanguageCode=request.language_code
    )

    return SentimentResponse(
        sentiment=response["Sentiment"],
        sentiment_score=response["SentimentScore"]
    )
