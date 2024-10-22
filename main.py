from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine #function that will create a engine
from sqlalchemy.orm import sessionmaker #function that will create a session
from sqlalchemy.ext.declarative import declarative_base #   

app = FastAPI()

DATABASE_URL = 'postgresql://postgres:vishal_404@localhost:5432/musicapp'
engine = create_engine(DATABASE_URL) #function calling the engine, requires databse url
#enginei is the starting point fro the sqlalchemy application thats need to connect to the database

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) #function that create the session objects when it called 
                                                #autocommit = False says that the session will not be automatically committed 
                                                # we should manually commit the session(session.commit)
                                                #autoflush = this autoflush determines whether the 
                                                # session automatically flush changes to the database before certain operations
                                                # setting it to False means that  Disables automatic flushing, waits until we give session.commint() or session.flush() 
                                                # which can improve performance in certain scenarios but requires manual control over when to flush.
                                                # important for transaction integrity and consistency 
                                                #bind parameter specefies which engine should it use 
db = SessionLocal()                                                                 

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

Base = declarative_base                         #Create a class user which will define the structure of the user model
                                                # in the database and then we can use that User to do multiple task like 
                                                # storing the data in the db and checking the user if he exists in the database 
                                                # if does not exsits it will create the database 
class User(Base)
@app.post('/signup')
def signup_user(user: UserCreate):
    #extracts the data that coming form the textfields
    print(user.name+"\n",user.email+"\n",user.password)
    #check if the user already exists in the database
    
    #add the user to the database
    pass 

#first api route has been created
#it should return something or it will return as null
#"async": "Async programming allows for non-blocking I/O operations, 
# making your application more efficient and scalable.",
#"await": "Await is used to wait for the completion of a coroutine, 
# allowing for asynchronous code to be written in a synchronous style."                        