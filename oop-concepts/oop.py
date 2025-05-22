class Car:
    #properties
    color='red'
    brand='toyota'
    #methods func
    def start(self):
        print("Engine startt")

#making object
my_car=Car()

#accessing properties / attributes
print(my_car.color)
print(my_car.brand)

#call methods
my_car.start()