from typing import List

class Human:
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Human):
    def _init_(self, name, age, student_id):
        super()._init_(name, age)
        self.student_id = student_id

    def get_details(self):
        return f"{super().get_details()}, Student ID: {self.student_id}"

class Teacher(Human):
    def _init_(self, name, age, employee_id):
        super()._init_(name, age)
        self.employee_id = employee_id

    def get_details(self):
        return f"{super().get_details()}, Employee ID: {self.employee_id}"

class Department:
    def _init_(self, name):
        self.name = name
        self.students = []
        self.teachers = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def get_details(self):
        details = f"Department: {self.name}\n"
        details += "Students:\n"
        for student in self.students:
            details += f"  - {student.get_details()}\n"
        details += "Teachers:\n"
        for teacher in self.teachers:
            details += f"  - {teacher.get_details()}\n"
        return details

class University:
    def _init_(self, name):
        self.name = name
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)

    def get_details(self):
        details = f"University: {self.name}\n"
        for department in self.departments:
            details += department.get_details() + "\n"
        return details

# Example usage
if _name_ == "_main_":
    # Create university
    uni = University("Digital University")

    # Create departments
    cs_department = Department("Computer Science")
    ee_department = Department("Mechanical Engineering")

    # Create students and teachers
    student1 = Student("Fariya", 20, "S123")
    student2 = Student("Saima", 22, "S456")
    teacher1 = Teacher("Dr. Ali", 45, "T789")
    teacher2 = Teacher("Dr.Bilal", 50, "T101")

    # Add students and teachers to departments
    cs_department.add_student(student1)
    cs_department.add_teacher(teacher1)
    ee_department.add_student(student2)
    ee_department.add_teacher(teacher2)

    # Add departments to university
    uni.add_department(cs_department)
    uni.add_department(ee_department)

    # Print university details
    print(uni.get_details())
