class Animal:  #parent /Base class
    def sound(self):
        print("Animal Sound")

class Dog(Animal):  #child class  inhert properties,methods from parent/base class
    def sound(self):
        print("meow!!!")

d=Dog()
d.sound()