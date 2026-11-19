#using pydantic which is a super killing feature which auto validates the input or the data
#doing post as a request body if we use name:str,age:int in the paramteres of the function it will be treated as the query parameter 

from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
  name:str
  age:int

@app.post("/create-user")
def create_user(user:User):
  return{
    "message":"user created",
    "data":user
  }