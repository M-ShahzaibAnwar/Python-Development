class Student():
    def __init__(self,name,rollNo):
        self.name=name
        self.rollNo=rollNo
    def display_info(self):
        print(f"name is {self.name}")
        print(f"Roll No is {self.rollNo}")


s=Student("Shahzaib","054")
s.display_info()