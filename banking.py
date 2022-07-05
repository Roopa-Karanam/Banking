import time
import datetime
class Account:
    """
    Represents an Account
    
    transactions	A list of Transaction instances
get_balance()	A method which returns the account balance
deposit(amount)	A method which creates a deposit transaction
withdraw(amount)	A method which creates a withdrawal transaction
    """
    transactions=[]
    def __init__(self):
        self.transactions = []
    
  
    def deposit(self,amount):        
        y=abs(amount)        
        x=Transaction(y)
        self.transactions.append(x)
       # return self.transactions+=x
    def withdraw(self, amount):
        y= abs(amount)
        y=y*-1
        x=Transaction(y)
        self.transactions.append(x)
        #return self.transactions+=x
    def get_balance(self):
        bal=0
        for i in range (0,len(self.transactions)):
            bal=+self.transactions[i]
        return bal
        
        
    
class Transaction():
    def __init__(self, amount, timestamp=None):
        """
        Extends the Person __init__ and requires an employee_id.
        """
        self.amount = amount
        self.timestamp=datetime.datetime.now()
        


    def __repr__(self):
       return 'Transaction(time: ={}, amount={})'.format(
            repr(self.amount),
            repr(self.timestamp),
            
        )
    
    def __str__(self):
            return 'Account(time: ={}, Balance={})'.format(
                 repr(self.balance),
                 repr(self.timestamp),
                 
             )

