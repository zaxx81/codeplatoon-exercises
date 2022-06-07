from asyncio.constants import ACCEPT_RETRY_DELAY
import csv, os
import imp
from classes.account import Account
from classes.owner import Owner

class Bank:

  def __init__(self, name) -> None:
    self.name = name
    self.accounts = Account.all_accounts()
    self.owners = Owner.all_owners()
    self.link_accounts()


  def link_accounts(self):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../support/account_owners.csv")
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            self.account_pair(*row)

  def account_pair(self, account_id, owner_id):
    pair_account = self.find_account(int(account_id))
    pair_owner = self.find_owners(int(owner_id))
    print(pair_account)
    print(pair_owner)
    pair_account.owner = pair_owner

  def find_account(self, id):
    for account in self.accounts:
      if account.id == int(id):
        return account

  def find_owners(self, id):
    for owner in self.owners:
      if owner.id == int(id):
        return owner
