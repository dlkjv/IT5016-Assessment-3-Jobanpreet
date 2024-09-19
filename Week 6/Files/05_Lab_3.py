"""
Week 6 Lab 
Question 3: Python program to print attributes of a car.
Author: Jobanpreet Singh
"""

class Car():
    def __init__(self, color,model, year):
        self.color = color
        self.model = model
        self.year = year

    def description(self):
        print(f"""
            {self.color}
            {self.model}
            {self.year}
            """)
        
car1 = Car("Black","Ford Mustang",2018)

car1.description()


    