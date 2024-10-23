from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker #function that will create a session

DATABASE_URL = 'postgresql://postgres:vishal_404@localhost:5432/musicapp'
engine = create_engine(DATABASE_URL) #function calling the engine, requires databse url
#enginei is the starting point fro the sqlalchemy application thats need to connect to the database

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine) 
                                                #function that create the session objects when it called 
                                                #autocommit = False says that the session will not be automatically committed 
                                                # we should manually commit the session(session.commit)
                                                #autoflush = this autoflush determines whether the 
                                                # session automatically flush changes to the database before certain operations
                                                # setting it to False means that  Disables automatic flushing, waits until we give session.commint() or session.flush() 
                                                # which can improve performance in certain scenarios but requires manual control over when to flush.
                                                # important for transaction integrity and consistency 
                                                #bind parameter specefies which engine should it use 
db = SessionLocal()  