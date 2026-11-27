#sqlalchemy
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session
from fastapi import FastAPI,Depends

app=FastAPI()

DATABASE_URL="sqlite:///./test.db"

engine=create_engine(
  DATABASE_URL,
  connect_args={"check_same_thread":False}
)                            #create_engine is a function used to connect the databse in sqlalchemy

#now we will handle operations in session db
sessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

class todo(Base):
  __tablename__="todos"

  id=Column(Integer,primary_key=True,index=True)
  title=Column(String)
  completed=Column(String)

Base.metadata.create_all(bind=engine)

#common function
def get_db():
  db=sessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/")
def home(db:Session=Depends(get_db)):
  return{
    "message":"Db connected successfully"
  }