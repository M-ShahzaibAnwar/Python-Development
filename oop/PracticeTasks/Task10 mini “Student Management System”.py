'''Student class with attributes: name, id, marks
Class method to calculate grade based on marks
Store multiple students in a list, show top scorer
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

# List to store student objects
students = [
    Student("Ali", 101, 78),
    Student("Sara", 102, 91),
    Student("John", 103, 67),
    Student("Mehak", 104, 45)
]

# Print all students with their grades
for student in students:
    print(f"{student.name} (ID: {student.id}) - Marks: {student.marks}, Grade: {student.cal_grade()}")

# Show the top scorer
top_student = max(students, key=lambda s: s.marks)
print(f"\n🏆 Top Scorer: {top_student.name} with {top_student.marks} marks and Grade: {top_student.cal_grade()}")
