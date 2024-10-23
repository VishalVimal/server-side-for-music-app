from fastapi import FastAPI
from models.base import Base
from routes import auth 
from database import engine

app = FastAPI()
app.include_router(auth.router, prefix='/auth')                                                   
Base.metadata.create_all(engine) #unites all the class that extends base so that it can 
                                 #create table based on the classes
                                

#first api route has been created
#it should return something or it will return as null
#"async": "Async programming allows for non-blocking I/O operations, 
# making your application more efficient and scalable.",
#"await": "Await is used to wait for the completion of a coroutine, 
# allowing for asynchronous code to be written in a synchronous style."                        