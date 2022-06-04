from classes.student import Student
from classes.staff import Staff

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()

    def student_roster(self):
        print("----Student Roster----")
        for student in self.students:
            print(student)
        print("\n")
   
    def staff_roster(self):
        print("----Staff Roster----")
        for staff in self.staff:
            print(staff)
        print("\n")
   
    def roster(self):
        print("=====Master Roster=====\n")

        self.student_roster()
        self.staff_roster()
        print("\n")
