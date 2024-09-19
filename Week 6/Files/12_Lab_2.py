"""
Week 6 Lab 2
Question 2: Python program to create banking system using encapsulation
Author: Jobanpreet Singh
"""

class Account:
    def __init__(self, owner, balance = 0):
        self.owner = owner #defines public attribute
        self.__balance = balance #defines private attribute

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"${amount} deposited")

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"${amount} withdrawn.")

        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance
    

account = Account("James",100)
print(account.owner)

account.deposit(65)
print(account.get_balance())
account.withdraw(35)
print(account.get_balance())
