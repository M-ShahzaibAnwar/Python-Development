'''Task 5: Create a class hierarchy
Parent class: Vehicle (method: start())

Child classes: Car, Motorcycle, Bus (override start())'''


class Vehicle:   #parent class
    def start(self):
        print("Engine Start!!!")
    
class Car(Vehicle):
    def start(self):
        print("Meow!!!")

class Motorcycle(Vehicle):
    def start(self):
        print("RATARATARARATARA")

class Bus(Vehicle):
    def start(self):
        print("HORRN!!!")


v=Vehicle()
v.start()

c=Car()
c.start()

m=Motorcycle()
m.start()

b=Bus()
b.start()

v.start()

vehicles = [Car(), Motorcycle(), Bus()]

for vehicle in vehicles:
    vehicle.start()
