from fastapi import FastAPI
from models import Person, PersonCreate
from store import get_people, add_person
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Lappiz Demo Api", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/getPeople", response_model=list[Person], status_code=200, operation_id="getPeople")
def getPeople():
    return get_people()

@app.post("/addPerson", response_model=Person, status_code=201, operation_id="addPerson")
def addPerson(person_data: PersonCreate):
    new_person = Person(
        nombre=person_data.nombre,
        correo=person_data.correo
    )
    return add_person(new_person)