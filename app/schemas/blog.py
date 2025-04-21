from pydantic import BaseModel

class BlogSchema(BaseModel):
    title: str
    content: str
    author: str
    published: bool

class BlogResponseSchema(BlogSchema):
    id: str