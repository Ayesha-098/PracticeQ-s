from abc import ABC, abstractmethod

class Appliance(ABC):
    def turn_on(self):
        print("Appliance is now ON")
    
    @abstractmethod
    def turn_off(self):
        pass

class WashingMachine(Appliance):
    def turn_on(self):
        super().turn_on()
        print("Washing Machine is now ON")
    
    def turn_off(self):
        print("Washing Machine is now OFF")

washingmachine = WashingMachine()
washingmachine.turn_on()
washingmachine.turn_off()
