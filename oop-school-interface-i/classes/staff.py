from classes.person import Person
import csv
class Staff(Person):
    pass
    # def __init__(self, employee_id):
    #     super().__init__

    def all_staff():

        individual_staff = []

        with open ('data/staff.csv', 'r' ) as staff_f :
            rows = csv.reader(staff_f, delimiter= ",")
            value = next(rows)
            for row in rows :
                individual_staff.append(Staff(*row))
        return individual_staff
