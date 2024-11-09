from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"message": "This is your posts"}

@app.post("/createpost")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"message": "The post has been created Successfully"}