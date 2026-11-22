#response models
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
  name:str
  age:int
  password:str

#creating response model
class UserResponse(BaseModel):#keep here what you want to show to the user
  name:str
  age:int

@app.get("/users",response_model=UserResponse) #keeps the password hidden from users (frontend ko wahi dikhega jo response model mein h)
def get_user():
  return{
    "name":"Tuhina",
     "age":20,
     "password":"12345"    
    }
