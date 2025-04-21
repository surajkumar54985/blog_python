from fastapi import APIRouter, HTTPException
from app.schemas.blog import BlogSchema, BlogResponseSchema
from app.crud.blog import add_blog, retrieve_blogs, update_blog, delete_blog

router = APIRouter(prefix="/blog", tags=["Blog"])

@router.post("/", response_model=BlogResponseSchema)
async def create_blog(blog: BlogSchema):
    blog_id = await add_blog(blog)
    return {"id": blog_id, **blog.dict()}

@router.get("/", response_model=list[BlogResponseSchema])
async def get_blogs():
    return await retrieve_blogs()

@router.put("/{blog_id}")
async def edit_blog(blog_id: str, blog: BlogSchema):
    updated = await update_blog(blog_id, blog)
    if updated:
        return {"message": "Blog updated successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")

@router.delete("/{blog_id}")
async def remove_blog(blog_id: str):
    deleted = await delete_blog(blog_id)
    if deleted:
        return {"message": "Blog deleted successfully"}
    raise HTTPException(status_code=404, detail="Blog not found")