import numpy as np 

class BankAccount:
    def __init__(self, name, balance, account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def withdraw(self, amount_withdrawed):
        """This function monitors how much you take out of your account. It will return false if you do not have sufficient funds."""
        if amount_withdrawed > self.balance or amount_withdrawed<0:
            print(f"Overdraft. You do not have enough money to withdraw ${amount_withdrawed}.")
            return False
        else:
            self.balance = self.balance - amount_withdrawed
            print(f"You have withdrawed ${amount_withdrawed} from your bank account.")
            return True

    def deposit(self, amount_deposited):
        """This function deposits the given amount and adds it to your previous balance"""
        self.balance = self.balance + amount_deposited
        print(f"You have deposited ${amount_deposited}!")
        return self.balance

    def current_balance(self):
        """This function prints your current balance."""
        print(f"Your current balance is ${self.balance}.")
        return f"Your current balance is ${self.balance}."

