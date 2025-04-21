from app.models.user import user_collection
from app.schemas.user import UserCreate
from bson import ObjectId

async def create_user(user: UserCreate):
    user_dict = user.dict()
    result = await user_collection.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict

async def get_user_by_email(email: str):
    user = await user_collection.find_one({"email": email})
    if user:
        user["id"] = str(user["_id"])
    return user
