#CRUD Operations using todo api
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]#to store the list

class Todo(BaseModel):
  id:int
  title:str
  completed:bool

#create api
@app.post("/todos")
def create_todo(todo:Todo):
  todos.append(todo)
  return{
    "message":"ToDO added",
    "data":todo
  }
#reading all data
@app.get("/todos")
def get_todo():
  return todos
#reading specific data
@app.get("/todos/{tid}")
def get_todoid(tid:int):
  for i in todos:
    if (i.id==tid):
      return {
        "message":"Data found",
        "data":i
      }
  return "Error! given id  not found"

#performing update operations
@app.put("/todos/{tid}")
def update_data(tid:int,updated_data:Todo):
  for index,todo in enumerate(todos):
    if (todo.id == tid):
       todos[index]=updated_data
       return{
         "message":"Data updated",
         "data":updated_data
       }
#performing delete

@app.delete("/todos/{tid}")
def delete_data(tid:int):
  for index,todo in enumerate(todos):
    if(todo.id==tid):
      data=todos.pop(index)
      return{
        "message":"Data deleted successfully",
        "deleted data":data
      }
  return {
    "message":"Matching id not found"
  }