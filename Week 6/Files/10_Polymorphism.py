"""
Program: Python program to understand polymorphism.
Author: Jobanpreet Singh
"""
class Device:
    def turn_on(self):
        pass
    
class TV(Device):
    def turn_on(self):
        return "TV is now on"

class Fan(Device):
    def turn_on(self):
        return "Fan is now spinning"
    
class Light(Device):    
    def turn_on(self):
        return "Light is now on"
    

#function that uses polymorphism

def activate_device(device):
    print(device.turn_on())

#create instance
tv = TV()
fan = Fan()
light = Light()

#use polymorphism
activate_device(tv)
activate_device(fan)
activate_device(light)