"""
Represents an Account

"""
import time
import datetime
class Account:
    '''
    Account class'''
 
    def __init__(self):
        '''init method'''
        self.transactions = []
    def deposit(self,amount):
        '''deposit method'''
        y_amount=abs(amount)
        x_amount=Transaction(y_amount)
        self.transactions.append(x_amount)
       # return self.transactions+=x
    def withdraw(self, amount):
        '''withdraw method'''
        y_amount= abs(amount)
        y_amount=y_amount*-1
        x_amount=Transaction(y_amount)
        self.transactions.append(x_amount)
        #return self.transactions+=x
    def get_balance(self):
        '''get balance method'''
        bal=0
        for transaction in self.transactions:
            bal = +transaction.amount
        return bal
class Transaction():
    '''Transaction class'''
    def __init__(self, amount, timestamp=None):
        """
       init method
        """
        self.amount = amount
        if timestamp is None:
            self.timestamp=datetime.datetime.now()
        else:
            self.timestamp=timestamp
    def __repr__(self):
        '''repr method'''
        return 'Transaction(timestamp: ={}, amount={})'.format(
            (self.timestamp),
            (self.amount))
    def __str__(self):
        '''str method'''
        return self.timestamp.strftime("%Y-%m-%d") + ": $ "+self.amount

