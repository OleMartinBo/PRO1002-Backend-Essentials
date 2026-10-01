# Exercise 3. Simple Class and Inheritance

# This is the Person class that includes the attributes name, age, and the greet() method.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f'Hello, {self.name}! You are {self.age} years old.')


#The Student class inherits from Person, adds an attribute student_id, and a method to print the student ID.
class Student(Person):
    def __init__(self,name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        
    def print_student_id(self):
        print(f'{self.name} Your student ID is: {self.student_id}')
        