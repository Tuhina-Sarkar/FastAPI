#middleware
from fastapi import FastAPI,Request

app=FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):
  print("Request recieved")

  response=await call_next(request)  #it means it waits while the control is passed to the next processing stage so the correspondinf route(if present executes and generates a response then ) the control is again passed to the middleware and it resumes its execution from the line imeediately after await

  print("Request sent")

  return response