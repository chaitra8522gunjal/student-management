
from fastapi import FastAPI

# ye code post api ke liye hai 
from pydantic import BaseModel 

app = FastAPI()

# ye code post api ke liye hai
class Student(BaseModel):
    id: int
    name: str
    marks: int


students = [
    {"id": 1, "name": "pooja", "marks": 85},
    {"id": 2, "name": "chaitra", "marks": 78}
]


@app.get("/")
def home():
    # return {"message": "Bind Mount is working!"}
    # return{"message": "My code updated without rebuilding Docker image!"}
    return{"message": "My code updated , again using docker mount !"}
    # return {"message": "my updated Student Management Docker API is working!"}


@app.get("/students")
def get_students():
    return students

# post api ke liye
@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())
    return {
        "message": "Student added successfully",
        "student": student
    }




# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def home():
#     return {"message": "Student Management API is working!"}


# FastAPI() — API application banata hai.
# @app.get("/") — home URL ke liye GET endpoint banata hai.
# home() — request aane par message return karta hai.
# return {...} — response JSON format mein bhejta hai.