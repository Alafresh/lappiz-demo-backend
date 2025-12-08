from pydantic import BaseModel, EmailStrn, Field

class Person(BaseModel):
    nombre: str = Field(..., min_length=4, max_length=60)
    correo: EmailStrn