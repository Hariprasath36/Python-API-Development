
import pytest
from jose import jwt
from app import schemas
from app.config import settings

    

# def test_root(client):
#     res=client.get("/")
#     print(res.json().get('message'))
#     assert res.json().get('message')=='Hello World'
#     assert res.status_code==200

def test_create_user(client):
    res=client.post("/users/",json={"email":"hello123@example.com","password":"password123"})   
    new_user = schemas.UserOut(**res.json()) 
    assert new_user.email =='hello123@example.com'  
    assert res.status_code==201    
   
def test_login_user(test_user,client):
    res=client.post("/login",data={"username":test_user['email'],"password":test_user['password']})   
   