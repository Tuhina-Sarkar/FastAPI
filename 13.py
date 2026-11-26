from fastapi import FastAPI,Depends   #Depends for dependency injection
#dependency injection means providing class or function whatever it needs
from pydantic import BaseModel

app=FastAPI()

#common logic 
def common_logic():
  return{
    "message":"Common logic executed"
  }

@app.get("/home")
def home(data=Depends(common_logic)):
  #we wrapped the common logic function inside the depends
  return data

