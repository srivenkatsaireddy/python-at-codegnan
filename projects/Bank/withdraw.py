from database import users
from emailsend import SingleEmailSend
def withdraw(account:int,withdraw_amount:int)-> str:
    curr_balance = users[account]['balance']
    if curr_balance >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        SingleEmailSend(to_email=users[account]["email"],subject="Withdrawl alert",body= f"{withdraw_amount} withdraw successful and current balance is :{users[account]['balance']}")
        return f"{withdraw_amount} withdraw successful and current balance is :{users[account]['balance']}"
    return "Insufficient Amount"