from fastapi import FastAPI,Depends

app=FastAPI()

#a depends function contaning reusable logic

def get_current_user():
  return{
    "User":"Tuhina Sarkar"
  }

@app.get("/user")
def users(user:str=Depends(get_current_user)):  #we are using the value returned by the function get_current_user by wrapping it inside depends
  return user

@app.get("/dashboard")
def dashboard(user:str=Depends(get_current_user)):
  return user