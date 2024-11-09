from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"message": "This is your posts"}

@app.post("/createpost")
def create_posts():
    return {"message": "The post has been created"}