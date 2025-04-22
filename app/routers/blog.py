from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from app.schemas.blog import BlogCreate
from app.services.blog_service import create_blog, list_blogs
from app.core.aws_s3 import upload_file_to_s3


router = APIRouter()

@router.post("/")
async def create(blog: BlogCreate):
    # Create a new blog by calling the service
    return await create_blog(blog)

@router.get("/")
async def get_all():
    # Get all blogs by calling the service
    return await list_blogs()

@router.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    url = upload_file_to_s3(file, folder="blog-images")
    return {"url": url}
