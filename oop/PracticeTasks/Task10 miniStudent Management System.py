'''Student class with attributes: name, id, marks
Class method to calculate grade based on marks
Store multiple students in a list, show top scorer
Add student

Show all students

Show top scorer

Search student by ID

Exit program


'''

class Student:
    def __init__(self, name, id, marks):
        self.name = name
        self.id = id
        self.marks = marks

    def cal_grade(self):
        if self.marks >= 85:
            return "A+"
        elif self.marks >= 80:
            return "A-"
        elif self.marks >= 72:
            return "B+"
        elif self.marks >= 62:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "D (Failed)"


students=[]
while True:
    print("1 :Add the Students--- ")
    print("2 :Show the All Students---")
    print("3 :Show Top Scorer Students---")
    print("4 :Seach Student by ID---")
    print("5 :Exit---")

    choice = input("Enter the Choice  1--5 :")
    if choice == "1":
        name=input("Enter the Name :")
        id=int(input("Enter the ID :"))
        marks=float(input("Enter thr Marks :"))
        students.append(Student(name,id,marks))
        print("---Student Add Successfully---")

    elif choice == "2":
        if not students:
            print("No Student to Show---")
        else:
            for s in students:
                print(f"Students are {s.name}---{s.id}----{s.marks}")
    
    elif choice == "3":
        if not students:
            print("No Student to SHow --")
        else:
            top_student=max(students, key=lambda  s: s.marks)
            for s in students:
                print(f"tOP students are {s.name}---{s.id}---{s.marks}---GRADE:{s.cal_grade()}-- ")

    elif choice == "4":
        search_id=input("Enter the STUDENT ID ---")
        found = False
        for s in students:
            if s.id==search_id:
                print(f"Student is : {s.name}--{s.id}---{s.marks}---{s.cal_grade()}") 
                found = True
                break
        if not found:
            print("No student with this id----")
    
    elif choice == "5":
        print("Exiting!!!THANK YOU---")
        break

    else:
        print("Invalid choice!!! please choose 1---5 :")

    

    

    
        
