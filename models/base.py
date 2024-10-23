from sqlalchemy.ext.declarative import declarative_base  


Base = declarative_base()                       #Create a class user which will define the structure of the user model
                                                # in the database and then we can use that User to do multiple task like 
                                                # storing the data in the db and checking the user if he exists in the database 
                                                # if does not exsits it will create the database 