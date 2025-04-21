from app.database import blog_collection
from app.models import Blog
from bson import ObjectId

def blog_helper(blog) -> dict:
    return {
        "id": str(blog["_id"]),
        "title": blog["title"],
        "": blog["content"],
        "author": blog["author"],
        "published": blog["published"],
    }

async def add_blog(blog: Blog):
    blog = await blog_collection.insert_one(blog.dict())
    return str(blog.inserted_id)

async def retrieve_blogs():
    blogs = []
    async for blog in blog_collection.find():
        blogs.append(blog_helper(blog))
    return blogs

async def update_blog(blog_id: str, blog: Blog):
    await blog_collection.update_one({"_id": ObjectId(blog_id)}, {"$set": blog.dict()})
    return True

async def delete_blog(blog_id: str):
    await blog_collection.delete_one({"_id": ObjectId(blog_id)})
    return True