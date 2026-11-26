#auth using depends
from fastapi import FastAPI,Depends,Header,HTTPException
#header is used to extract information on the http request provided by the user to the api

app=FastAPI()

#common logic containing function
def verify_user(token:str=Header(None)):#a default value none is given to header
  if(token!="secret"):
    raise HTTPException(
      status_code=401,
      detail="Authentication failed"
    )
  return{
    "User":"Authenticated successfully"
  }

@app.get("/secure-access")
def secure(user:str=Depends(verify_user)):
  return{
    "message":"Secure Data accessed",
    "User":user
  }

#Dependency injection is a pattern framework in which dependencies required by a function or a class are provided outside instead of creating it inside
#depends is a function of fastapi to declare a dependency.fastapi automatically executes the depends function and injects its returned value to the path operation function

  #real use case of dependency injection:       authorisation access , database connect,  reuse logic
  #in Auth system use of dependency is to verify tokens or to secure endpoints
