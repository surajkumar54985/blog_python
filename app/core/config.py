from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Settings:
    # MongoDB connection string
    MONGO_URI: str = os.getenv("MONGO_DETAILS")
    
    # JWT Authentication settings
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    
    # AWS credentials
    AWS_ACCESS_KEY: str = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY: str = os.getenv("AWS_SECRET_KEY")
    AWS_BUCKET_NAME: str = os.getenv("AWS_BUCKET_NAME")

settings = Settings()
