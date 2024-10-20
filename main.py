from fastapi import FastAPI
app = FastAPI() #creating a fast api instance

#creating a api route
@app.post('/') 
def test(q: str):
    return 'Hello World' #first api route has been created
                         #it should return something or it will return as null
