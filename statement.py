import pandas as pd
import matplotlib.pyplot as plt


class Statement:
    def __init__(self, path: str = 'statements/statement.csv', balance: int = 0):
        self.path = path
        self.start_balance = balance
        self.ledger = None

    def load(self):
        transactions = pd.read_csv(self.path, dtype={'amount':int, 'date':str})
        date = pd.to_datetime(transactions['date'], yearfirst=True)
        transactions.drop('date', axis=1, inplace=True)
        transactions['date'] = date
        transactions.sort_values(by=['date', 'amount'], ascending=[True, True])
        transactions.reset_index(drop=True)
        self.ledger = transactions

    def balance(self):
        self.ledger['balance'] = 0

        for i in range(self.ledger.shape[0]):
            if i == 0:
                previous_balance = self.start_balance
            else:
                previous_balance = self.ledger.at[i - 1, 'balance']
            self.ledger.at[i, 'balance'] = previous_balance + self.ledger.at[i, 'amount']

    def plot(self):
        plt.plot(self.ledger['date'], self.ledger['balance'] / 100)
        plt.show()
