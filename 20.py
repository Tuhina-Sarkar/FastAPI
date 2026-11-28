#CRUD operations with db
from sqlalchemy import create_engine,Integer,Column,String
from sqlalchemy.orm import sessionmaker,Session,declarative_base
from fastapi import FastAPI,Depends,HTTPException

app=FastAPI()

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread":False}
)

sessionLocal=sessionmaker(bind=engine)#created session for db operations

base=declarative_base()


class Todo(base):#a model for the table 
  __tablename__="Todos"

  id=Column(Integer,primary_key=True,index=True)
  title=Column(String)
  completed=Column(String)

base.metadata.create_all(bind=engine)

def get_db():
  db=sessionLocal()
  try:
    yield db
  finally:
    db.close()

#CRUD operations

#create api i.e.  Post
@app.post("/todos")
def create_todo(title:str,db:Session=Depends(get_db)):
  todo=Todo(title=title,completed="False")
  db.add(todo)
  db.commit()
  db.refresh(todo)
  return {
    "message":"todo created successfully",
    "data":todo
  }
#read api(read all data)
@app.get("/todos")
def get_todo(db:Session=Depends(get_db)):
  todos=db.query(Todo).all() #query to get all the data

  return{
    "Total ":len(todos),
    "data":todos
  }

#read one by one based on specific id
@app.get("/todos/{todo_id}")
def get_to(todo_id:int,db:Session=Depends(get_db)):
  todo=db.query(Todo).filter(Todo.id==todo_id).first()   

  if not todo:
    raise HTTPException(
      status_code=404,
      detail="Todo not found"
    )
  else:
    return todo

#update data based on id
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,title:str,db:Session=Depends(get_db)):
  todo=db.query(Todo).filter(Todo.id==todo_id).first()

  if not todo:
    raise HTTPException(
          status_code=404,
          detail="Todo not found"
        )
  else:
    todo.title=title

    db.commit()  #saves the changes 
    db.refresh(todo)  #updates the db object with the latest data

    return{
      "message":"Data updated successfully",
      "data":todo
    }

  
#delete operation
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int,db:Session=Depends(get_db)):
  todo=db.query(Todo).filter(Todo.id==todo_id).first()
  if not todo:
    raise HTTPException(
      status_code=404,
      detail="Todo not found"
     )
  else:
    db.delete(todo)
    db.commit()
    return{
      "message":"Data deleted successfully"
    }
