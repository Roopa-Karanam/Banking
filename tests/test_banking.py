from banking import Account
from banking import Transaction
import datetime
datetime.datetime.now()

def test_transaaction_amount():
    transaction = Transaction(100)
    assert transaction.amount == 100
def test_transaaction_timestamp():
    transaction = Transaction(100)
    assert transaction.timestamp == datetime.datetime.now()
'''def test_deposit():
    account=Account()
    account.deposit(100)
    assert  account.get_balance()==100
'''
