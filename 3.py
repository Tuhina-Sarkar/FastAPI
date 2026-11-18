#dynamic routes using path parameters
from fastapi import FastAPI
app=FastAPI()

@app.get("/users/{user_id}")#validating data types
def get_users(user_id:int):#
  return {"user_id":user_id}
