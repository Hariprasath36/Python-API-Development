import pytest
from app import schemas

def test_get_all_posts(authorized_client,test_posts):
   res=authorized_client.get("/posts/")
