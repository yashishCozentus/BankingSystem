from CustomerDetails.Customer import Customer
from AccountDetails.Account import Account
from TransactionDetails.Transaction import Transaction

#obj = Customer('123CD','Yashish','BBSR','1234567890')
#obj1 = Customer('124CD','Mohanty','BBSR','12344444')

#acc = Account('123ID',obj.name,100)
#acc2 = Account('124ID',obj1.name,1000)

#print(acc.get_account_info())
#print(acc2.get_account_info())
#
#tran1 = Transaction('Tran1',acc.account_id,acc.account_id,1000)
#tran2 = Transaction('Tran2',acc.account_id,acc2.account_id,10000)
#
#print(tran1.get_transaction_details())
#print(tran2.get_transaction_details())
#print(Transaction.get_transaction_history(acc2.account_id))
#print(Transaction.transaction_history)

#Customer 1: Customer ID: "C001", Name: "John Doe", Address: "123 Main St", Phone Number: "555-1234"
Customer1 = Customer('C001','John Doe','123 Main St','555-1234')

#Customer 2: Customer ID: "C002", Name: "Jane Smith", Address: "456 Elm St", Phone Number: "555-5678"
Customer2 = Customer('C002','Jane Smith','456 Elm St','555-5678')


#John Doe's Savings Account: Account Number: "S001"
JD_SA = Account('S001',Customer1)
#John Doe's Checking Account: Account Number: "C001"
JD_CA = Account('C001',Customer1)
#Jane Smith's Savings Account: Account Number: "S002"
JS_SA = Account('S002',Customer2)
#Jane Smith's Checking Account: Account Number: "C002"
JS_CA = Account('C002',Customer2)

#Deposit $1000 into John Doe's Savings Account.
print(JD_SA.deposit(1000))

#Withdraw $200 from Jane Smith's Checking Account.
print(JS_CA.withdraw(200))

#Perform a transfer of $300 from John Doe's Checking Account to Jane Smith's Savings Account.
Trans1 = Transaction('T1',JD_CA,JS_SA,300)
Tran2 = Transaction('T2',JD_SA,JS_SA,1000)
#Retrieve and display the balance of all four accounts.

#John Doe
print('John Doe Saving Acc Bal: ',JD_SA.get_balance())
print('John Doe Checking Acc Bal: ',JD_CA.get_balance())

#Jane Smith
print('Jane Smith Checking Acc Bal: ',JS_CA.get_balance())
print('Jane Smith Saving Acc Bal:',JS_SA.get_balance())


print("Transactions done by the account of Jane Smith's Savings Acc",Transaction.get_transaction_history(JS_SA))
print()
print()
print("Transactions done by the account of John Doe's Savings Acc",Transaction.get_transaction_history(JD_SA))

print()
print()
print(Transaction.transaction_history)





