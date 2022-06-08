import csv
import os.path
from classes.owner import Owner

class Account:

  def __init__(self, id, balance, open_date) -> None:
    self.id = int(id)
    self.balance = balance
    self.open_date = open_date
    self.owner = None
    self.check_min()
    
  # Does not allow a negative opening balance. Will set balance to $0 instead
  def check_min(self):
    try:
      if int(self.balance) < 0:
        raise Exception(f'Opening Balance Error: Balance may not be negative')
      print(f'Creating a new account {self.id} with a starting balance of ${self.balance}')
    except:
      self.balance = 0
      print(f'Creating a new account {self.id} with a starting balance of ${self.balance}')
  
  def __str__(self) -> str:
    return f'Account ID: {self.id}, Balance: {self.balance}'

  def withdraw(self, amount):
    try:
      if (self.balance - amount) < 0:
        raise Exception(f'Withdrawal Error: Balance may not be negative')
      print(f'Withdrawing ${amount} from your account...')
      self.balance -= amount
      self.show_balance()
    except:
      print(f'Invalid withdrawal amount! Your balance is ${self.balance}.')

  def deposit(self, amount):
    print(f'Depositing ${amount} from your account...')
    self.balance += amount
    self.show_balance()

  def show_balance(self):
    print(f'Your current balance is ${self.balance}')

  # def set_owner(self, owner):
  #   self.owner = owner

  # Class Methods
  def all_accounts():
    accounts = []

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../support/accounts.csv")
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            accounts.append(Account(*row))
    
    return accounts
