from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BlogBase(BaseModel):
    title: str
    content: str
    author: str
    image_url: Optional[str] = None  # 👈 Add this

class BlogCreate(BlogBase):
    pass

class BlogOut(BlogBase):
    id: str
    created_at: datetime