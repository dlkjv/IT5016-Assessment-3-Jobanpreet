"""
Program: Python program to define a class related to person information
Author: Jobanpreet Singh
"""

class Person():
    def __init__(self,name, age):
        self.name = name #initialize the name attribute
        self.age = age #initialize the age attribute

person1 = Person("James", 30)
person2 = Person("Jessica", 25)

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)

