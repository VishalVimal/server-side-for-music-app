from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
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