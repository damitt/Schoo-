from fastapi import FastAPI
from .endpoints import students, scores

app = FastAPI()

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(scores.router, prefix="/scores", tags=["scores"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Scores API"}
