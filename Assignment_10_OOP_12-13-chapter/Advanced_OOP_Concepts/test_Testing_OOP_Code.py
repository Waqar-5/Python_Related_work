# test_bank.py
import pytest
from Testing_OOP_Code import BankAccount

# Test object creation
def test_create_account():
    account = BankAccount("Alice", 100)
    assert account.owner == "Alice"
    assert account.balance == 100

# Test deposit method
def test_deposit():
    account = BankAccount("Bob", 50)
    account.deposit(30)
    assert account.balance == 80

# Edge case: deposit 0
def test_deposit_zero():
    account = BankAccount("Bob", 50)
    with pytest.raises(ValueError):
        account.deposit(0)

# Test withdraw method
def test_withdraw():
    account = BankAccount("Charlie", 100)
    account.withdraw(40)
    assert account.balance == 60

# Edge case: withdraw more than balance
def test_withdraw_insufficient_funds():
    account = BankAccount("Charlie", 100)
    with pytest.raises(ValueError):
        account.withdraw(200)

# Exception on negative balance at initialization
def test_negative_initial_balance():
    with pytest.raises(ValueError):
        BankAccount("Dave", -50)
