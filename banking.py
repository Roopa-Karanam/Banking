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
    transactions=''
    
    def __init__(self, first_name, last_name):
        self.balance=0

    def __str__(self):
         """Returns the full name."""
         return self.get_transactions()  

    def __repr__(self):
        """Returns an expression which can be used to recreate this object."""  
        return self.get_transactions()

    '''def get_transactions(self):
        """Returns the full name."""
        
    
    def get_balance(self):
        return get_transactions()
    
    def deposit(self,amount):        
        y=abs(amount)        
        x=Transaction(y)
       # return self.transactions+=x
    def withdraw(self, amount):
        y= abs(amount)
        y=y*-1
        x=Transaction(y)
        #return self.transactions+=x
        
        '''
      
    


class Transaction():
    def __init__(self, amount, timestamp=None):
        """
        Extends the Person __init__ and requires an employee_id.
        """
        self.amount = amount
        self.timestamp=datetime.datetime.now()


    def __repr__(self):
       return 'Account(time: ={}, amount={})'.format(
            repr(self.amount),
            repr(self.timestamp),
            
        )
    
    def __str__(self):
            return 'Account(time: ={}, Balance={})'.format(
                 repr(self.balance),
                 repr(self.timestamp),
                 
             )