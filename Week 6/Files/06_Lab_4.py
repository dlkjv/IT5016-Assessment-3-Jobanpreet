"""
Week 6 Lab
Question 4: Python program to print Car information
Author: Jobanpreet Singh
"""

class Car():
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(f"The {self.color} {self.model} is driving")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped")

    def display_info(self):
        print(f"Car Info: {self.year} {self.color} {self.model}")

car1 = Car("Black","Ford Mustang", 2021)

car1.drive()
car1.stop()
car1.display_info()
