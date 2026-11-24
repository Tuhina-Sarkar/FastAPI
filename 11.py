#status codes 
from fastapi import FastAPI,HTTPException

app=FastAPI()
#status codes using status_code
@app.post("/create_user",status_code=400)
def create_user():
  return{
    "message":"user created"
  }
#custom response
@app.get("/users")
def get_users():
  return {
    "status":"Success",
    "message":"user fetched",
    "data":{
      "name":"Tuhina",
      "age":21
    }
  }
#error  handling
@app.get("/users/{user_id}")
def get_user(user_id:int):
  if user_id!=1:
    raise HTTPException(
      status_code=404,
      detail="User Not Found"
    )
  return{
    "id":1,
    "name":"Tuhina"
  }
