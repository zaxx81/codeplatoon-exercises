class Person:
    def __init__(self, name, age, role, id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.id = id

    def __str__(self) :
        return f'Name: {self.name}\tRole: {self.role}\tID: {self.id}'