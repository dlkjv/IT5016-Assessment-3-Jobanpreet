"""
Week 6 Lab
Question 2: Python program to calculate Area and Perimeter of a rectangle.
Author: Jobanpreet Singh
"""

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self): 
        return 2 * (self.width + self.height)
    
rect = Rectangle(4,5)
print(f"Area of Rectangle: {rect.area()}")
print(f"Perimeter of Rectangle: {rect.perimeter()}")
