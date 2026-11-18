#multiple routes
from fastapi import FastAPI
app=FastAPI()

#home route symbolized by "/"
@app.get("/")
def home():
  return {"message":"Welcome to FastAPI"} 
#about route
@app.get("/about")
def about():
  return {"message":"This is about page"}

#users route
@app.get("/users")
def users_me():
  return {
    "users":["Tuhina","Taniya"]
  }
