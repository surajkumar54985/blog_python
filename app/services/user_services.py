from app.core.database import db
from app.schemas.user import UserCreate, UserLogin
from uuid import uuid4
from app.utils.mongo import convert_objectid
from bson import ObjectId
from app.utils.security import hash_password, verify_password
from app.core.aws_ses import send_confirmation_email
from app.core.aws_step import start_email_verification_step_function

async def create_user(user: UserCreate):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise Exception("Email already registered.")
    
    token = uuid4().hex
    user_dict = user.dict()
    user_dict["password"] = hash_password(user.password)
    user_dict["verified"] = False
    user_dict["token"] = token

    await db.users.insert_one(user_dict)

    # # send confirmation email here
    # send_confirmation_email(user.email, token)

    # Start the Step Function instead of sending email directly
    await start_email_verification_step_function(user.email, token)

    return {"msg": "User created. Check your email for confirmation."}

async def resend_confirmation_email(email: str):
    user = await db.users.find_one({"email": email})
    if not user:
        raise Exception("User not found.")
    if user["verified"]:
        raise Exception("User already verified.")

    token = uuid4().hex
    await db.users.update_one({"_id": user["_id"]}, {"$set": {"token": token}})
    send_confirmation_email(email, token)

    return {"msg": "Confirmation email resent."}



async def login_user(user: UserLogin):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user:
        raise Exception("Invalid credentials.")

    if not verify_password(user.password, db_user["password"]):
        raise Exception("Invalid credentials.")

    if not db_user["verified"]:
        raise Exception("Email not verified.")

    return {"msg": "Login successful."}


async def confirm_email(token: str):
    user = await db.users.find_one({"token": token})
    if not user:
        raise Exception("Invalid token.")
    await db.users.update_one({"_id": user["_id"]}, {"$set": {"verified": True}})
    return {"msg": "Email confirmed."}
