# Ek function alag tareeqon se behave karta hai
class Cat:
    def speak(self):
        print("meow")
class Dog:
    def speak(self):
        print("Bark")

def animal_sound(animal):
        animal.speak()

c=Cat()
d=Dog()

animal_sound(c)
animal_sound(d)