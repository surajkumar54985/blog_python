from fastapi import FastAPI
from app.routers import blog
from app.routers import user
from app.routers import sentiment_router

app = FastAPI()

app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(sentiment_router.router, prefix="/sentiment", tags=["Sentiments"])

@app.get("/")
def root():
    return {"message": "Welcome to Blog App"}
