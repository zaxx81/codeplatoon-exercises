from classes.school import School 
from classes.student import Student
from classes.staff import Staff
from classes.person import Person

school = School('Ridgemont High') 


print(school.name)

student_info = {'name' : 'Diana', 'password' : 'password', 'id' : 12345, 'age' : 17, 'role' : 'Student'}
Diana = Student(**student_info)

# school.staff_roster()
# school.student_roster()
school.roster()



# print(school.staff) 

# print(school.students)
# print(student_list)
