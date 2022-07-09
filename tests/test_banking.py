''' tests for module banking.py'''
from datetime import datetime
from banking import Transaction
from banking import Account
def test_transaaction_amount():
    '''
    test for amount

    Returns
    -------
    None.

    '''
    transaction = Transaction(100)
    assert transaction.amount == 100
def test_transaaction_timestamp():
    '''
    test for timestamp

    Returns
    -------
    None.

    '''
    transaction = Transaction(100)
    assert transaction.timestamp == datetime.now()
def test_deposit():
    """
    testing deposit

    Returns
    -------
    None.

    """
    test_account=Account()
    test_account.deposit(100)
    test_account.deposit(200)
    test_account.deposit(300)
    assert len(test_account.transactions)==3
def test_withdraw():
    '''
    testing withdraw

    Returns
    -------
    None.

    '''
    test_account=Account()
    test_account.withdraw(100)
    test_account.withdraw(200)
    test_account.withdraw(300)
    assert len(test_account.transactions)==3
def test_get_balance():
    '''
    testing get_balance

    Returns
    -------
    None.

    '''
    test_account=Account()
    test_account.withdraw(100)
    test_account.deposit(100)
    test_account.deposit(200)
    assert test_account.get_balance()==200
def test_transactions():
    '''
    testing transactions

    Returns
    -------
    None.

    '''
    test_transactions=Transaction(100, datetime(2023,12,12))
    assert test_transactions.amount==100
    assert test_transactions.timestamp==datetime(2023,12,12)
    
    