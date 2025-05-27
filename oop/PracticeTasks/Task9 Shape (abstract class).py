'''Task 8: Shape (abstract class)
Abstract method: area()

Child classes: Rectangle, Circle implement area()'''

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.width

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2  #pi r square

#cannot make object of parent class bcz its abstract class
r=Rectangle(5,6)
r.area()
print(f"Area of Rectangle is : {r.area()}")

c=Circle(2)
c.area()
print(f"Area of Cicle : {c.area()}" )