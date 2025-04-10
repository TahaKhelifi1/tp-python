# backend/models.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class Department(BaseModel):
    id: str
    name: str
    code: str  # e.g., "CS" for Computer Science

class Formation(BaseModel):
    id: str
    title: str
    description: str
    department_id: str  # Reference to Department
    credits: int

class Student(BaseModel):
    id: str
    name: str
    email: EmailStr
    hashed_password: str
    department_id: str
    enrolled_formations: List[str] = []  # Formation IDs
    created_at: datetime = datetime.now()