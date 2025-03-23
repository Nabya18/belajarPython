"""
# Class Methods = Allow operation related to the class itself
# Take (cls) as the first parameter, which represent the class itself

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that don't need access to the instance or class data
# Class methods = Best for class-level data or require access to the class itself
"""

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1 # student object created, increment the count by 1
        Student.total_gpa += gpa

    def get_info(self):
        return f"{self.name} has a GPA of {self.gpa}"

    @classmethod
    def get_count(cls): # cls = class itself
        return f"Total students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count}"

student1 = Student("Spongebob", 3.5)
student2 = Student("Patrick", 3.2)
student3 = Student("Squidward", 3.8)
student4 = Student("Sandy", 4.0)

print(Student.get_count()) # 0 students
print(Student.get_average_gpa()) # 0