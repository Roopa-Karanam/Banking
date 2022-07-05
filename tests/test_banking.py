from banking import Account
from banking import Transaction
import datetime

def test_transaaction_amount():
    transaction = Transaction(100)
    assert transaction.amount == 100
def test_transaaction_timestamp():
    transaction = Transaction(100)
    assert transaction.timestamp == datetime.datetime.now()    
#def test_transaaction_timestamp_given():
#   transaction = Transaction(100,'2022-07-05 12:40:42.068734')
#   assert transaction.timestamp == '2022-07-05 12:40:42.068734'

'''def test_transaction_repr():
    trans = Transaction(
        amount=100
        
        )
    expected = ("Account( amount:=100, timestamp:="+ str(datetime.datetime.now())
    assert repr(trans) == expected '''
    

