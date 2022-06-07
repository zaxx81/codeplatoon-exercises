from classes.expenses import Expenses

class Budget:
  def __init__(self, name) -> None:
    self.name = name
    self.income_monthly = 0
    self.transactions = Expenses.objects()

  def __str__(self) -> str:
    pass

  def add_expense(self):
    pass

  def remove_expense(id):
    pass

  def show_budget():
    pass
  