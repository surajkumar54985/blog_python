from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Connect to MongoDB using the URI from the config file
client = AsyncIOMotorClient(settings.MONGO_URI)

# Specify the database name here (e.g., 'blog_db')
db = client.get_database('blog_db')  # Or you can directly use 'blog_db' in the URI
