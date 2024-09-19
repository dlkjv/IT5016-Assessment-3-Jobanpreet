"""
Week 6 Lab 
Question 1: Python program to print introduction by using class.
Author: Jobanpreet Singh
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")

person1 = Person("Sukh", 20)
person1.greet()

