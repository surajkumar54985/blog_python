from fastapi import FastAPI
from app.routers import blog

app = FastAPI()

app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])

@app.get("/")
def root():
    return {"message": "Welcome to Blog App"}
