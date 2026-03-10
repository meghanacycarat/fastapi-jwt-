from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()  #instance of our fastapi 

@app.get("/")
def home():
    return {"Mssg":"hello"}

# @app.get("/login/id")
# def login():
#     pass    

@app.get("/greet/")
def greet(name:str , age:Optional[int]=None):
    return { "MEssage ":f"hello,{name} and age is {age}" }

class Student(BaseModel):
    name : str
    age : int
    roll : int

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name" : student.name,
        "age": student.age,
        "roll": student.roll
    }

