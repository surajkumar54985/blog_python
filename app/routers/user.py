from fastapi import APIRouter, HTTPException, Query
from app.schemas.user import UserCreate, UserLogin

from app.services.user_services import create_user, login_user, confirm_email

router = APIRouter()

@router.post("/signup")
async def signup(user: UserCreate):
    try:
        return await create_user(user)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(user: UserLogin):
    try:
        return login_user(user)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))

@router.get("/confirm")
async def confirm(token: str = Query(...)):
    try:
        return await confirm_email(token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
