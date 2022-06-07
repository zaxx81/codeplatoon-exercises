from classes.bank import Bank
from classes.account import Account
from classes.owner import Owner

# myAccount = Account(1234, -100.00)
# myAccount.withdraw(200)
# myAccount.deposit(500)
# myAccount.withdraw(100)

# print(myAccount._owner)
# owner1 = Owner(14,'Morales','Wanda','9003 Gerald Hill','Honolulu','Hawaii')
# myAccount.set_owner(owner1)
# print(myAccount._owner)

my_bank = Bank("USBB")
# for account in Account.accounts:
#   print(account)

# for owner in Owner.owners:
#   print(owner)

# Account.account_pair(1217, 14)
acct = 1217
print(f'Searching for account # {acct}...')
print(f'Found {my_bank.find_account(acct).owner}')