studentList = []


class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def average_mark(self):
        if len(self.marks) > 0:
            return sum(self.marks) / len(self.marks)


def create_student():
    name = input("Please enter the name of the new student: ")
    studentData = Student(name)

    return studentData


def add_marks(student, mark):
    student.marks.append(mark)


def print_student_details(student):
    print('''The Students Name is : {0},
            whose marks are {1}, with an Average of {2}
            '''.format(student.name, student.marks, student.average_mark())
          )


def print_student_list(students):
    for i, stud in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(stud)


def menu():
    selection = input("Enter 'p' to Print the student list,"
                      " 's' to add a new Student,"
                      " 'a' to Add a mark to a student"
                      " or 'q' to quit."
                      " Enter Selection: ")

    while selection != 'q':
        if selection == 'p':
            print_student_list(studentList)

        elif selection == 's':
            studentList.append(create_student())

        elif selection == 'a':
            student_i_d = int(input("Enter the Student ID to add a mark to: "))
            student = studentList[student_i_d]
            new_mark = int(input("Enter the new mark to be added: "))
            add_marks(student, new_mark)

        else:
            print("That is not a valid selection")

        selection = input("Enter 'p' to Print the student list,"
                          " 's' to add a new Student,"
                          " 'a' to Add a mark to a student"
                          " or 'q' to quit."
                          " Enter Selection: ")


menu()
