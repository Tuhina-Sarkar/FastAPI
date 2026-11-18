#query parameters
from fastapi import FastAPI
app=FastAPI()


@app.get("/users")
def get_users(name:str=None):#optional parameters
  return{"name":name}

@app.get("/products")
def get_users(limit:int=10):#default parameters
  return {"Limit":limit}

@app.get("/items")
def get_users(name:str=None,price:int=0):#multiple query params
  return{"name":name,"price":price}