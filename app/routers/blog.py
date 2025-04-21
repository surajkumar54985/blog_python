from fastapi import APIRouter, HTTPException
from app.schemas.blog import BlogCreate
from app.services.blog_service import create_blog, list_blogs

router = APIRouter()

@router.post("/")
async def create(blog: BlogCreate):
    # Create a new blog by calling the service
    return await create_blog(blog)

@router.get("/")
async def get_all():
    # Get all blogs by calling the service
    return await list_blogs()
