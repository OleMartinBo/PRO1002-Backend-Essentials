# Exercise 3. Simple Class and Inheritance

#Define a Person class that has attributes name and age and a method greet() that prints a greeting.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f'Hello, {self.name}! You are {self.age} years old.')

p1 = Person("Ole", 27)
p1.greet() 

#Define a Student class that inherits from Person and adds an attribute student_id.
#In your main script, create a Student object and call its greet() method.
#Print the student's student_id as well.