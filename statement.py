import pandas as pd


class Statement:
    def __init__(self):
        self.path = 'statements/statement.csv'
        self.transactions = None
        self.ledger = None
        self.start_balance = 0

    def load(self):
        transactions = pd.read_csv(self.path, dtype={'amount':int, 'date':str})
        date = pd.to_datetime(transactions['date'], yearfirst=True)
        transactions.drop('date', axis=1, inplace=True)
        transactions['date'] = date
        transactions.sort_values(by=['date', 'amount'], ascending=[True, True], inplace=True)
        self.transactions = transactions

    def balance(self):
        self.transactions['balance'] = 0

        for i in range(self.transactions.shape[0]):
            if i == 0:
                previous_balance = self.start_balance
            else:
                previous_balance = self.transactions.at[i-1, 'balance']
            self.transactions.at[i, 'balance'] = previous_balance + self.transactions.at[i, 'amount']
