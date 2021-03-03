from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass 

    @abstractmethod
    def horn(self):
        pass 



class Car(Vehicle):
    def wheels(self):
        return 4 

    def horn(self):
        return "nnn"



car = Car()
car.wheels()
    