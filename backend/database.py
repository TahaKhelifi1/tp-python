# backend/database.py
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import IndexModel

client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.student_management

# Create indexes
async def create_indexes():
    await db.students.create_indexes([
        IndexModel([("email", 1)], unique=True),
        IndexModel([("department_id", 1)]),
    ])
    await db.formations.create_index([("department_id", 1)])