''' Task 7: Employee class with Inheritance
Parent: Employee → name, salary

Child: Manager → has extra attribute: department

Method: show_details() (override in Manager)
'''

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show_details(self):
        print(f"detaisl!!! : {self.name} has salary {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name,salary)
        self.department = department
    
    def show_details(self):
        print(f"Details !!! : {self.name} has salary {self.salary} in department {self.department}")


#make objects and pass name through constructors
emp=Employee("shahzaib",500)
mng=Manager("Ali",500,"CS")

emp.show_details()
mng.show_details()

