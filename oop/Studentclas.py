''' Task 2: Create a Student class
Attributes: name, age, roll_no

Method: is_adult()  return True if age ≥ 18, else False'''

class Student:
    def __init__(self,name,age,roll_no):
        self.name=name
        self.age=age
        self.roll_no=roll_no

    def is_adult(self):
        if self.age>=18:
            return True
        else:
            return False

s1=Student("shahzaib",21,54)
s2=Student("Abd",15,61)

print(f"{s1.name} is adult : {s1.is_adult()}" )
print(f"{s2.name} is adult : {s2.is_adult()}" )