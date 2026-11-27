#sqlite db doesnt need to be installed we just need to import it to use
import sqlite3
from fastapi import FastAPI

app=FastAPI()
#to establish a connection we use connect func which takes two parameters : connect("file where we want to store the database","here we check wether same thread is not being used")
conn=sqlite3.connect("test.db",check_same_thread=False) #now our databse is connected

cursor=conn.cursor()#to run the sql query

cursor.execute("""
CREATE TABLE IF NOT EXISTS todos(
       id INTEGER PRIMARY KEY,
       title TEXT,
       completed TEXT
      )
""")
conn.commit()#to save the changes made 

@app.get("/")
def home():
  return {
    "message":"SQlite connected successfully!"
  }