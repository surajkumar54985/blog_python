from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str
    language_code: str = "en"

class SentimentResponse(BaseModel):
    sentiment: str
    sentiment_score: dict
