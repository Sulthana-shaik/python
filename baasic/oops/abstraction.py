from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

p = UPI()
p.pay(500)

print("-------example2------")
#Abstract class

class vechicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#class inheritence from abs class
class Car(vechicle):
    def start(self):
        print("car is start")

    def stop(self):
        print("car is stopping")
# Object creation (outside class)
my_car = Car()
my_car.start()
my_car.stop()