
from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str  
    published: bool =True

class PostCreate(BaseModel):
    pass

class Post(BaseModel):
    title: str
    content: str
    published: bool

