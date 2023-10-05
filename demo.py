import time

class Customer:
    def __init__(self, customer_id, name, address, phone_number):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def get_customer_info(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_number}"

class Account:
    def __init__(self, account_number, customer, initial_balance=0.0):
        self.account_number = account_number
        self.customer = customer
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

class Transaction:
    transaction_history = []

    def __init__(self, transaction_id, source_account, destination_account, amount):
        self.transaction_id = transaction_id
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def get_transaction_details(self):
        return f'Transaction ID: {self.transaction_id}\n' \
               f'Source Account: {self.source_account}\n' \
               f'Destination Account: {self.destination_account}\n' \
               f'Amount: {self.amount}\n' \
               f'Timestamp: {self.timestamp}'

def get_transaction_history(account):
    return [transaction.get_transaction_details() for transaction in Transaction.transaction_history if
            account in (transaction.source_account, transaction.destination_account)]

# Create two customer objects
customer1 = Customer("C001", "John Doe", "123 Main St", "555-1234")
customer2 = Customer("C002", "Jane Smith", "456 Elm St", "555-5678")

# Create two account objects for each customer
john_savings = Account("S001", customer1)
john_checking = Account("C001", customer1)
jane_savings = Account("S002", customer2)
jane_checking = Account("C002", customer2)

# Deposit $1000 into John Doe's Savings Account
john_savings.deposit(1000.0)

# Withdraw $200 from Jane Smith's Checking Account
jane_checking.withdraw(200.0)

# Perform a transfer of $300 from John Doe's Checking Account to Jane Smith's Savings Account
if john_checking.withdraw(300.0) and jane_savings.deposit(300.0):
    transaction1 = Transaction("T001", john_checking, jane_savings, 300.0)
    Transaction.transaction_history.append(transaction1)

# Retrieve and display the balance of all four accounts
print(f"John Doe's Savings Account Balance: ${john_savings.get_balance()}")
print(f"John Doe's Checking Account Balance: ${john_checking.get_balance()}")
print(f"Jane Smith's Savings Account Balance: ${jane_savings.get_balance()}")
print(f"Jane Smith's Checking Account Balance: ${jane_checking.get_balance()}")

# Create transaction objects
deposit_transaction = Transaction("D001", john_savings, None, 1000.0)
withdraw_transaction = Transaction("W001", None, jane_checking, 200.0)

# Display the details of each transaction
print("\nTransaction Details:")
print(deposit_transaction.get_transaction_details())
print(withdraw_transaction.get_transaction_details())

# Get transaction history for John Doe's Checking Account
john_checking_history = get_transaction_history(john_checking)
print("\nTransaction History for John Doe's Checking Account:")
for transaction_details in john_checking_history:
    print(transaction_details)
