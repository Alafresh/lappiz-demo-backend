from fastapi import FastAPI, HTTPException, status
from .models import Person, PersonCreate
from .store import get_people, add_person, email_exists
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lappiz Demo Api", version="1.0.0")

origins = [
    "http://localhost:4200",
    "https://lappiz-demo-frontend.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Lappiz Demo API esta on"}

@app.get("/getPeople", response_model=list[Person], status_code=200, operation_id="getPeople")
def getPeople():
    return get_people()

@app.post("/addPerson", response_model=Person, status_code=201, operation_id="addPerson")
def addPerson(person_data: PersonCreate):
    if email_exists(person_data.correo):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El correo {person_data.correo} ya está registrado"
        )
    
    new_person = Person(
        nombre=person_data.nombre,
        correo=person_data.correo
    )
    return add_person(new_person)