from typing import List
from models import Person

__people: List[Person] = [{
    'nombre': 'Juan Guillermo',
    'correro': 'alafresh16@gmail.com'
}]

def get_people() -> List[Person]:
    return __people

def add_person(person: Person) -> Person:
    __people.append(person)
    return person