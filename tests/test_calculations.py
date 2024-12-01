import pytest
from app.calculations import add, divide, multiply, subtract

@pytest.mark.parametrize("num1,num2,expected",[
    (3,2,5),
    (7,3,10),
    (2,5,7)
])
def test_add(num1,num2,expected):
    print("testing add function")
    assert add(num1,num2)== expected

def test_subtract():
    print("testing subtract function")
    assert subtract(5,3)== 2

def test_multiply():
    print("testing multiply function")
    assert multiply(5,3)== 15

def test_divide():
    print("testing divide function")
    assert divide(20,5)== 4