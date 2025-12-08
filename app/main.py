from fastapi import FastAPI

app = FastAPI(title="Lappiz Demo Api", version="1.0.0")

@app.get("/getPeople")
def getPeople():
    pass

@app.post("/addPerson")
def addPerson():
    pass