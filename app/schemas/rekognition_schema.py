from pydantic import BaseModel
from typing import List, Optional

class Label(BaseModel):
    Name: str
    Confidence: float

class RekognitionResponse(BaseModel):
    Labels: List[Label]
