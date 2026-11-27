#Logging middleware-real world example of middleware 
#that tracks every request that in what amount of time it is executing 
from fastapi import FastAPI,Request
import time

app=FastAPI()
# why middleware is asynchronous? =>so that our application remains high performance and it can handle multiple requests effectively 
#middleware is global whereas dependency injection is per route
@app.middleware("http")
async def log_middleware(req:Request,call_next):#call_next=yeh request ko next app (actually api function) tak bhejti h aur response return bhi krta h

   start_time=time.time()

   response=await call_next(req)

   process_time=time.time()-start_time

   print(f"Path:{req.url.path} | Time:{process_time}")

   return response


#real use cases of middleware
#authentication,logging,api tracking or monitoring,debugging,validate requests , to execute rate limiter , to add or remove from header,security check ,har request mein common logic execute krna hota h tab bhi middle ware use hota h