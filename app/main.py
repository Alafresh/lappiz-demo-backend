from fastapi import FastAPI
from models import Person
from store import get_people, add_person

app = FastAPI(title="Lappiz Demo Api", version="1.0.0")

@app.get("/getPeople", response_model=list[Person], status_code=200)
def getPeople():
    return get_people()

@app.post("/addPerson", response_model=Person, status_code=201)
def addPerson(person: Person):
    return add_person(person)