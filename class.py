import random
class Student:
    def __init__(student_info, name, ID, Age, gpa):
        student_info.name = name
        student_info.Age = Age
        student_info.gpa = gpa
        student_info.ID = ID
reading = open('../List Exercise/fullname.txt', 'r')
for x in reading:
    noNewLine = x.rstrip()
    student_info = Student(noNewLine, random.randint(50, 1000), random.randint(18, 35), round(random.uniform(1.9, 4.0), 2))
    print("Name:", student_info.name, "Age:", student_info.Age, "ID:", student_info.ID, "GPA:", student_info.gpa)
