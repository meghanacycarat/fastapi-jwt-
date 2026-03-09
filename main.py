from fastapi import FastAPI

app = FastAPI()  #instance of our fastapi 

@app.get("/")
def home():
    return {"Mssg":"hello"}

# @app.get("/login/id")
# def login():
#     pass    

@app.get("/greet/")
def greet(name:str , age:int=None):
    return { "MEssage ":f"hello,{name} and age is {age}" }