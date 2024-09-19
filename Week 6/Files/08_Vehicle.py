class Vehicle:
    def __init__(self) -> None:
        pass

    def start(self):
        print("Vehicle started.")

    def stop(self):
        print("Vehicle stopped.")

class Car(Vehicle):
    def horn(self):
        print("Honk!Honk!")


car = Car()
car.start()
car.horn()
car.stop()
