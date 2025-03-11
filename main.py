from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

# Initialisation de l'application FastAPI
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Autoriser le frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

# Modèle Pydantic pour valider les données d'un étudiant
class Student(BaseModel):
    id: int
    name: str
    age: int

# Base de données fictive pour stocker les étudiants
students_db = []

# Endpoint pour ajouter un étudiant
@app.post("/students/", response_model=Student)
def create_student(student: Student):
    """
    Ajoute un étudiant à la base de données.
    - **student**: Objet Student contenant l'ID, le nom et l'âge.
    """
    students_db.append(student)
    return student

# Endpoint pour récupérer tous les étudiants
@app.get("/students/", response_model=List[Student])
def get_students():
    """
    Retourne la liste de tous les étudiants.
    """
    return students_db

# Endpoint pour récupérer un étudiant par son ID
@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    """
    Retourne un étudiant spécifique par son ID.
    - **student_id**: ID de l'étudiant à rechercher.
    """
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    """
    Supprime un étudiant spécifique par son ID.
    - **student_id**: ID de l'étudiant à supprimer.
    """
    for index, student in enumerate(students_db):
        if student.id == student_id:
            del students_db[index]
            return {"message": "Student deleted successfully"}
    raise HTTPException(status_code=404, detail="Student not found")
