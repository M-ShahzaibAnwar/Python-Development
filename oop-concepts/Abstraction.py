#hide backend details only see interface ui
from abc import ABC,abstractmethod #abc → This is Python’s Abstract Base Class module.##A decorator that marks a method as abstract (i.e., it must be defined in any subclass).
#ABC → A built-in base class that lets you create abstract classes.
class Shape(ABC):  #in python for abstraction we use ABC module,now Shape class is absrtact class,only be inherited,cannot use directly
    @abstractmethod # This tells Python: “Any class that inherits Shape MUST define area().”
    def area(self): #every shape has a area method
        pass   #Placeholder since there's no actual code here.

class Circle(Shape): #as i inhertis from Shape,so it also has area method
    def area(self):
        print("Area of circle")   

c=Circle()
c.area()