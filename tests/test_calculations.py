import pytest
from app.calculations import add, divide, multiply, subtract,BankAccount,InsufficientFunds

@pytest.fixture
def zero_bank_account():
    return BankAccount(0)
@pytest.fixture
def bank_account():
    return BankAccount(50)

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

def test_bank_set_initial_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_bank_default_amount():
    bank_account = BankAccount(50)
    assert bank_account.balance == 50

def test_withdraw():
    bank_account = BankAccount(50)
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit():
    bank_account = BankAccount(50)
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_intrest():
    bank_account = BankAccount(50)
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55
