from typing import List
from models import Person

__people: List[Person] = [
    Person(nombre="Juan guillermo", correo="alafresh16@gmail.com")
]

def get_people() -> List[Person]:
    return __people

def add_person(person: Person) -> Person:
    __people.append(person)
    return person

def email_exists(correo: str) -> bool:
    return any(person.correo.lower() == correo.lower() for person in __people)