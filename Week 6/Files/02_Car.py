"""
Program: Python program 
Author: Jobanpreet Singh
"""

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model


    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

car1 = Car("Black", "Mustang")
car2 = Car("Blue", "Challenger")

car1.drive()
car2.stop()


