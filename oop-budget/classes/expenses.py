import csv
import os.path
from socket import INADDR_UNSPEC_GROUP

class Expenses:
  id_counter = 0

  def __init__(self, description, category, amount) -> None:
    self.id = Expenses.id_counter
    self.description = description
    self.category = category
    self.amount = amount
    Expenses.id_counter += 1

  @classmethod
  def objects(cls):
    expenses = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    my_file = '../data/expenses.csv'
    path = os.path.join(my_path, my_file)
    
    try:
      with open(path) as csvfile:
        print(f'Reading {my_file}...')
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f'Adding expense "{row}')
            expenses.append(Expenses(**dict(row)))
      return expenses

    except FileNotFoundError:
      print('Could not import expenses.csv...Creating a new file...')
      header = ['description', 'category', 'amount']

    try:
      with open(path, 'w') as csvfile:
        print(f'Creating file {my_file}...')
        writer = csv.writer(csvfile)
        writer.writerow(header)
    except:
      print(f'Could not create {my_file}')

  def __str__(self) -> str:
    return f'{self.description}\t{self.category}\t{self.amount}'
