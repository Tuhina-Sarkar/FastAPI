#first fastapi code
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
  return {"message":"Hello world From FASTAPI venv"}