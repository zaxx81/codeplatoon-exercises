from classes.bank import Bank
from classes.account import Account
from classes.owner import Owner
from classes.savings_account import SavingsAccount
from classes.checking_account import CheckingAccount

# myAccount = SavingsAccount(1234, 10000, "Today")
# print(myAccount.add_interest(0.0025))
# print(myAccount.show_balance())
# myAccount = Account(1234, -8.00, "Today")
# myAccount.withdraw(90)
# myAccount.deposit(500)
# myAccount.withdraw(100)

# print(myAccount._owner)
# owner1 = Owner(14,'Morales','Wanda','9003 Gerald Hill','Honolulu','Hawaii')
# myAccount.set_owner(owner1)
# print(myAccount._owner)

# my_bank = Bank("USBB")
# # for account in Account.accounts:
# #   print(account)

# # for owner in Owner.owners:
# #   print(owner)

# # Account.account_pair(1217, 14)
# acct = 1217
# print(f'Searching for account # {acct}...')
# print(f'Found {my_bank.find_account(acct).owner}')

myAccount = CheckingAccount(1234, 100, "Today")
myAccount.withdraw_using_check(20)
myAccount.withdraw_using_check(20)
myAccount.withdraw_using_check(20)

myAccount.reset_checks()
myAccount.withdraw_using_check(20)


# print(myAccount.show_balance())