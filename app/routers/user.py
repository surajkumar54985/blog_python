from fastapi import APIRouter, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.crud.user import create_user, get_user_by_email

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
async def register_user(user: UserCreate):
    existing_user = await get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = await create_user(user)
    return new_user
