import pytest
from app.calculations import add, subtract, multiply, divide, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    print("creating an empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    print("Creating bank account with initial balance 50")
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 5),
    (4, 5, 9),
    (9, 0, 9),
])
def test_add(num1, num2, expected):
    print("testing add function")
    assert add(num1, num2) == expected

def test_subtract():
    assert subtract(6,2) == 4

def test_multiply():
    assert multiply(6,2) == 12


def test_divive():
    assert divide(6,2) == 3


def test_bank_set_initial_amount(bank_account):
    print("testing bank account initial balance as 50")
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    print("testing zero bank account")
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(30)
    assert bank_account.balance == 20

def test_deposit(bank_account):
    bank_account.deposit(10)
    assert bank_account.balance == 60

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 20, 30),
    (400, 300, 100),
])

def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_fund(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)