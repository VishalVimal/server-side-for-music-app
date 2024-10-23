import uuid
import bcrypt
from fastapi import HTTPException
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter
from database import db

router = APIRouter()

@router.post('/signup')
def signup_user(user: UserCreate):
    #extracts the data that coming form the textfields
    #print(user.name+"\n",user.email+"\n",user.password) -> we have extracted the user data
    #check if the user already exists in the database
    user_db = db.query(User).filter(User.email == user.email).first()
    if user_db:
        raise HTTPException(400,'User with the same email already exists!') #using http exception we can return the error code 
        #return -> using return will return the message but not as an error as error 400
    
    hash_password = bcrypt.hashpw(user.password.encode(),bcrypt.gensalt(16)) #using bcrypt to hash password, salt -> random piece of data to create a unique hash, 
                                                            # even if the user has two user has same password that hash value differs
    user_db = User(id=str(uuid.uuid4()),email=user.email,password=hash_password,name=user.name)
    #add the user to the database
    db.add(user_db)
    db.commit()
    db.refresh(user_db) #refresh all the instance in the userdb and stores the correct value
    return user_db

