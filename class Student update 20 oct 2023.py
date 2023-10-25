class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self. marks = marks

    def __str__(self):
      return f'{"*"*20} \n {self.roll} {self.name} {self.marks}'

students = []

def return_student():
    roll = int(input("Enter roll number of student"))
    for student in students:
        if student.roll == roll:
            return student

def add_student():
    roll = int(input("Enter roll number here:"))
    name = input("Enter name here:")
    marks = int(input("Enter marks here:"))

    stu = Student(roll, name, marks)
    students.append(stu)
    print("Student Added")

def show_student():
    for student in students:
        print(student)

def delete_student():
    result = return_student()
    if result:
        students.remove(result)
    else:
        print("No such student")

def update_student():
    result = return_student()

    if result:
        ch = int(input('what do you wants to update\n'\
             '1. Name\n'\
             '2. Marks\n'))
        match ch:
            case 1:
                newname = input("Enter new name")
                result.name = newname
            case 2:
                newmarks = int(input("Enter new marks"))
                result.marks = newmarks
    else:
        print("No such student")

while True:
    ch = int(input("\n\nEnter Choice:\n1.Add Student\t\n2.Show All Student info\n3.Update Student info\n4.Delete Student info\n5.Exit"))
    match ch:
        case 1:
            add_student()
        case 2:
            show_student()
        case 3:
            update_student()
        case 4:
            delete_student()
        case 5:
            print("Exit")
            break
        case _:
            print("Default Value")

print("PROGRAM END")
            
            
