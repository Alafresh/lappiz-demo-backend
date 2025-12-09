from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from datetime import datetime

class PersonCreate(BaseModel):
    nombre: str = Field(..., min_length=4, max_length=60)
    correo: EmailStr

class Person(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    nombre: str = Field(..., min_length=4, max_length=60)
    correo: EmailStr
    fecha: datetime = Field(default_factory=datetime.now)