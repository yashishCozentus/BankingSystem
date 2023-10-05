#import sys
#sys.path('C:\Users\CZ0259\Banking System\src\CustomerDetails\Customer.py')
from CustomerDetails.Customer import Customer

class Account:
    def __init__(self, account_id, customer, balance=0):
        self.account_id = account_id
        self.customer = customer
        self.balance = balance
    
    def get_account_info(self):
        return f"Account ID: {self.account_id}\n Customer: {self.customer}\n Balance: {self.balance}\n"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if (0 < amount) and (amount <= self.balance):
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
if __name__ == '__main__':
    obj = obj = Customer('123CD','Yashish','BBSR','1234567890')
