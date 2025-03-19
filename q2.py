# - Create a base class Vehicle with a method start(). Create a subclass Car that overrides start() and calls super().start(). Now create another subclass ElectricCar that overrides start() again.


class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car is starting")

class ElectricCar(Car):
    def start(self):
        super().start()
        print("Electric Car is starting")

electricCar = ElectricCar()
electricCar.start()
