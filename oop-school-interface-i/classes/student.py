
from classes.person import Person

import csv

class Student(Person):
    def all_students():

        individual_students = []

        with open ('data/students.csv', 'r' ) as student_f :
            rows = csv.reader(student_f, delimiter= ",")
            value = next(rows)

            for row in rows :
                individual_students.append(Student(*row))
        return individual_students
