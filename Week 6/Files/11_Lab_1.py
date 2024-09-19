"""
Week 6 Lab 2
Question 1: Python program to print the car's battery capacity.
Author:Jobanpreet Singh
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

class ElectricCar(Car):
    def __init__(self, color, model, year, battery_capacity):
        super().__init__(color, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity:{self.battery_capacity} kWh")

my_electric_car = ElectricCar("Black", "Ford Mustang", 2023, 76)
my_electric_car.drive()
my_electric_car.stop()
my_electric_car.display_info()
