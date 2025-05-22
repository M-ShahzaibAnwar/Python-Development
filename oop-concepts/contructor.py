#when object make ,then contructor automatically means
class Car:
    def __init__(self,color,model):  #__init__ is a constructor method
        self.color=color   #properties of object
        self.model=model

    def start(self):
        print(f"this is my {self.color} {self.model}")

#object creation
my_car=Car("blue","mehran")   #constuctor called when object created
my_car.start()
