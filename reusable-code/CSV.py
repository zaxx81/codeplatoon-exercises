import csv, os

def myReader(self):
    read_list = []

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/csvfile.csv")
    with open(path) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            read_list.append(*row)

def myReader(self):
    read_list = []

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../data/csvfile.csv")
    with open(path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            read_list(**row)