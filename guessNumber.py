import numpy as np
studentList = []

def create_student():
    name = input("Please enter the name of the new student: ")
    studentData = {
        'name': name,
        'marks': []
    }

    return studentData


def add_marks(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    if len(student['marks']) > 0:
        return sum(student['marks']) / len(student['marks'])


def print_student_details(student):
    print('''The Students Name is : {0},
            whose marks are {1}, with an Average of {2}
            '''.format(student['name'], student['marks'], calculate_average_mark(student))
          )


def print_student_list(students):
    for stud in students:
        print_student_details(stud)


student = create_student()
print(calculate_average_mark(student))
add_marks(student, 70)

print(calculate_average_mark(student))
