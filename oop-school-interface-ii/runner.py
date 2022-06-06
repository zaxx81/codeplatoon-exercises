#runner.py 
from classes.school import School 

school = School('Ridgemont High') 

def menu():
  print("\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n")

  return input('Please enter an option: ')

mode = menu()
while mode != '5':
  if mode == '1':
    school.list_students()
  elif mode == '2':
    student_id = input('Enter student id: ')
    student = school.find_student_by_id(student_id)
    print(str(student))
  elif mode == '5':
    print('Goodbye!')
    exit
  else:
      print('Invalid option.')
  
  mode = menu()
