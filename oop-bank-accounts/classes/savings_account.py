from classes.account import Account

class SavingsAccount(Account):

  def __init__(self, id, balance, open_date) -> None:
    super().__init__(id, balance, open_date)

  def check_min(self):
    try:
      if int(self.balance) < 10:
        raise Exception(f'Opening Balance Error: Balance may not be negative')
      print(f'Creating a new account {self.id} with a starting balance of ${self.balance}')
    except:
      print(f'Sorry, you need at least $10 to open a savings account')

  def withdraw(self, amount):
    withdraw_fee = 2
    try:
      if (self.balance - amount) < 10 + withdraw_fee:
        raise Exception(f'Withdrawal Error: Balance may be below $10')
      print(f'Withdrawing ${amount} plus a $2 fee from your account...')
      self.balance -= (amount + withdraw_fee)
      self.show_balance()
    except:
      print(f'Invalid withdrawal amount! Your balance is ${self.balance}.')

  def add_interest(self, rate):
    interest = self.balance * rate
    self.balance += interest
    return interest