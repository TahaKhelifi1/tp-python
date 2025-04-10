from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from motor.motor_asyncio import AsyncIOMotorClient
from models import Student, Department, Formation

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Connexion MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.student_management

# Endpoints Étudiants
@app.post("/students/register")
async def register_student(student: Student):
    await db.students.insert_one(student.dict())
    return {"message": "Étudiant enregistré avec succès !"}

# Endpoints Formations
@app.get("/formations")
async def get_formations():
    formations = await db.formations.find().to_list(100)
    return formations