#pydantic models
from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):#we create schema based on the class here we are creating user schema and validate the data inside the class
  name:str
  age:int
  email:str

@app.post("/create_user")
def create_user(user:User):
  return {
    "message":"User created successfully",
    "data":user
  }

