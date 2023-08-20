"""Creation of bank account with options of withdraw and deposit money, get balance"""
import uuid
from datetime import date


class Transaction:
    def __init__(self, summary: float,  operation: str, date_today):
        self.summary = summary
        self.operation = operation
        self.date_today = date_today

    def __repr__(self):
        return f'Sum: {self.summary} ; Operation: {self.operation} ; date: {self.date_today}'


class BankAccount:
    def __init__(self, name: str, balance: float = 0.0):
        self.name = name
        self.id = uuid.uuid1()
        self.balance = balance
        self.transactions = []

    def __repr__(self):
        return f'ID: {self.id} | Name: {self.name} | Balance: {self.balance} | Transactions {self.transactions}'

    def add_transaction(self, summary: float, operation: str, date_today):
        """Add transaction on the list of transactions"""
        self.transactions.append(Transaction(summary, operation, date_today))

    def get_balance(self):
        """Get balance on the bank account"""
        return f'Balance: {self.balance}'

    def withdraw_money(self, amount):
        """Withdraw money from the bank account (fee 1% included)"""
        if self.balance >= amount:
            self.balance = self.balance - (amount + amount * 0.1)
            self.add_transaction(self.balance, "Withdraw", date.today())
            print(f"You withdrew {amount + amount * 0.1}$")
        return self.balance

    def deposit(self, amount):
        """Deposit money on the bank account (fee 1% included)"""
        self.balance = self.balance + amount * 0.9
        self.add_transaction(self.balance, "Deposit", date.today())
        print(f"You deposited {amount * 0.9}$")
        return self.balance


# usage example
b_a1 = BankAccount("B1", 100.13)
print(b_a1.get_balance())
b_a1.withdraw_money(10)
print(b_a1.get_balance())
b_a1.deposit(20)
print(b_a1)
