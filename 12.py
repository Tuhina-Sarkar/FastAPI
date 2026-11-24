from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse

app=FastAPI()

#custom exceptions
class UserNotFoundException(Exception):
  def __init__(self,name:str):
    self.name=name

#global exception handling
@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request:Request,exc:UserNotFoundException):
  return JSONResponse(
    status_code=404,
    content={
      "status":"error",
      "message":f"User{exc.name} not found"
    }
  )

@app.get("/user/{name}")
def get_user(name:str):
  if(name!="Tuhina"):
    raise UserNotFoundException(name) #custom error
  return {
    "name":name
  }
