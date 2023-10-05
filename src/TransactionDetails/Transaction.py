import time
class Transaction:

    transaction_history = []

    def __init__(self, transaction_id, source_account, destination_account, amount):
        self.transaction_id = transaction_id
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        
        #Transfer
        if source_account.withdraw(self.amount) == True:
            destination_account.deposit(self.amount)
            print('Successful')
        else:
            print('Cannot Perform the Transaction')

        #Transaction.transaction_history[self.transaction_id] = (self.amount,self.timestamp,self.source_account,self.destination_account)
        Transaction.transaction_history.append((self.amount,self.timestamp,self.source_account.account_id,self.destination_account.account_id))


    def get_transaction_details(self):
        return f'Transaction ID: {self.transaction_id}\n' \
               f'Source Account: {self.source_account}\n' \
               f'Destination Account: {self.destination_account}\n' \
               f'Amount: {self.amount}\n' \
               f'Timestamp: {self.timestamp}\n'


    def get_transaction_history(account):
        req_history = []
        for i in Transaction.transaction_history:
            if account.account_id in i:
                req_history.append(i)
        return req_history
