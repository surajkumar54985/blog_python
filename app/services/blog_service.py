from app.core.database import db
from app.schemas.blog import BlogCreate
from bson import ObjectId
from app.utils.mongo import convert_objectid
from bson import ObjectId

# Function to create a blog
async def create_blog(blog: BlogCreate):
    blog_dict = blog.dict()
    result = await db.blogs.insert_one(blog_dict)

    created_blog = await db.blogs.find_one({"_id": result.inserted_id})
    return convert_objectid(created_blog)

# Function to list blogs
async def list_blogs():
    blogs = []
    async for blog in db.blogs.find():
        blogs.append(convert_objectid(blog))
    return blogs



