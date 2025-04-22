from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# BlogCreate schema for request validation (creating a blog)
class BlogCreate(BaseModel):
    title: str
    content: str
    author: str
    image_url: str
    created_at: Optional[datetime] = datetime.utcnow()
