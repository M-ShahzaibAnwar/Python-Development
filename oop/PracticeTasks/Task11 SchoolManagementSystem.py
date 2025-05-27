'''✨ BONUS CHALLENGE
Lets say youre building a school management system:

Classes: Student, Teacher, Course

Students enroll in courses

Teachers teach courses

You can search students by course, see grades, assign teachers'''

# ---------- Classes ----------

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.enrolled_courses = []

    def enroll(self, course):
        self.enrolled_courses.append(course)

    def view_courses(self):
        if not self.enrolled_courses:
            print(f"{self.name} is not enrolled in any courses.")
        else:
            print(f"{self.name} is enrolled in:")
            for course in self.enrolled_courses:
                print(f"- {course.name}")


class Teacher:
    def __init__(self, name, teacher_id):
        self.name = name
        self.teacher_id = teacher_id
        self.assigned_courses = []

    def assign_course(self, course):
        self.assigned_courses.append(course)

    def view_courses(self):
        if not self.assigned_courses:
            print(f"{self.name} has not been assigned any courses.")
        else:
            print(f"{self.name} teaches:")
            for course in self.assigned_courses:
                print(f"- {course.name}")


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id
        self.teacher = None
        self.students = []

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def add_student(self, student):
        self.students.append(student)

    def get_info(self):
        print(f"\nCourse: {self.name} ({self.course_id})")
        if self.teacher:
            print(f"Teacher: {self.teacher.name}")
        else:
            print("No teacher assigned yet.")
        
        if self.students:
            print("Students enrolled:")
            for student in self.students:
                print(f"- {student.name}")
        else:
            print("No students enrolled yet.")


# ---------- Controller ----------

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, name, student_id):
        student = Student(name, student_id)
        self.students.append(student)
        print(f"Student '{name}' added successfully.")

    def add_teacher(self, name, teacher_id):
        teacher = Teacher(name, teacher_id)
        self.teachers.append(teacher)
        print(f"Teacher '{name}' added successfully.")

    def add_course(self, name, course_id):
        course = Course(name, course_id)
        self.courses.append(course)
        print(f"Course '{name}' added successfully.")

    def enroll_student_in_course(self, student_id, course_id):
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if student and course:
            student.enroll(course)
            course.add_student(student)
            print(f"Student '{student.name}' enrolled in course '{course.name}'.")
        else:
            print("Student or Course not found.")

    def assign_teacher_to_course(self, teacher_id, course_id):
        teacher = next((t for t in self.teachers if t.teacher_id == teacher_id), None)
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if teacher and course:
            course.assign_teacher(teacher)
            teacher.assign_course(course)
            print(f"Teacher '{teacher.name}' assigned to course '{course.name}'.")
        else:
            print("Teacher or Course not found.")

    def show_all_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(f"{student.name} (ID: {student.student_id})")

    def show_all_teachers(self):
        if not self.teachers:
            print("No teachers found.")
        else:
            for teacher in self.teachers:
                print(f"{teacher.name} (ID: {teacher.teacher_id})")

    def show_all_courses(self):
        if not self.courses:
            print("No courses found.")
        else:
            for course in self.courses:
                course.get_info()


# ---------- Menu Loop ----------

def menu():
    school = SchoolSystem()

    while True:
        print("\n===== School Management Menu =====")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Add Course")
        print("4. Enroll Student in Course")
        print("5. Assign Teacher to Course")
        print("6. Show All Students")
        print("7. Show All Teachers")
        print("8. Show All Courses")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            name = input("Enter student name: ")
            sid = input("Enter student ID: ")
            school.add_student(name, sid)

        elif choice == "2":
            name = input("Enter teacher name: ")
            tid = input("Enter teacher ID: ")
            school.add_teacher(name, tid)

        elif choice == "3":
            name = input("Enter course name: ")
            cid = input("Enter course ID: ")
            school.add_course(name, cid)

        elif choice == "4":
            sid = input("Enter student ID: ")
            cid = input("Enter course ID: ")
            school.enroll_student_in_course(sid, cid)

        elif choice == "5":
            tid = input("Enter teacher ID: ")
            cid = input("Enter course ID: ")
            school.assign_teacher_to_course(tid, cid)

        elif choice == "6":
            school.show_all_students()

        elif choice == "7":
            school.show_all_teachers()

        elif choice == "8":
            school.show_all_courses()

        elif choice == "9":
            print("Thank you! Exiting the system.")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 9.")

# ---------- Run the Program ----------
menu()
