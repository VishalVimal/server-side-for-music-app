from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary #function that will create a engine 
from models.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(TEXT, primary_key = True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary) #text1234 -> we going to hash the password 