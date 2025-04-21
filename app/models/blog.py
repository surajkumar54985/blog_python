from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Blog(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = datetime.utcnow()
