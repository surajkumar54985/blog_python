from fastapi import FastAPI
from app.routers import blog, user

app = FastAPI()

app.include_router(blog.router, prefix="/blogs", tags=["Blogs"])
app.include_router(user.router, prefix="/users", tags=["Users"])
# app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Blog API!"}