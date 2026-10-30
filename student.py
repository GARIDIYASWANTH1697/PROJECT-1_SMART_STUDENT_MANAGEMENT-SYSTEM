from module import Student
from database import load_data,save_data
SUBJECTS = [
    "Math",
    "Physics",
    "English",
    "Computer",
    "Chemistry"
]

def Add_student():
    students = load_data()
    try:
        student_id = int(input("Enter Student ID: "))
        if student_id <=0:
            print("ID should be positive")
            return
    except ValueError:
        print("invalid input")
        return
    for student in students:
        if student["student_id"]== student_id:

            print("student already found")
            return
    student_name = input("Enter Student Name: ").strip().title()
    if student_name == "":
        print("student should not be empty")
        return
    try:
        age = int(input("Enter Student Age: "))
        if age <=0:
            print("age should be greater than 0 ")
            return
    except ValueError:
        print("invalid input")
        return
    course = input("Enter Student Course: ").strip().upper()
    if course == "":
        print("course should not be empty")
        return

    subjects = {}
    for subject in SUBJECTS:
        try:
            marks = float( input(f"Enter {subject} Marks: "))
            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100")
                return
            subjects[subject] = marks
        except ValueError:
            print("Invalid input")
            return
    new_student = Student(student_id,student_name,age,course,subjects )
    students.append(new_student.to_dict())
    save_data(students)
    print("student added successfully")

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def pass_fail(marks):
    if marks >= 50:
        return "PASS"
    else:
        return "FAIL"

def show_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    for student in students:
        # print(student) is ki form ko kutch is thra se 
        result_card(student)
def search_student():
    students = load_data()
    if not students:
        print("No students found.")
        return
    try:
        search_id = int(input("Enter Student ID to search: "))
        if search_id <=0:
            print("ID should be positive")
            return
    except ValueError:
        print("invalid input")
        return
    found = False
    for student in students:
        if student["student_id"] == search_id:
            result_card(student)
            found = True
            break
    if not found:
        print("Student not found.")
def update_student():

    students = load_data()

    if not students:
        print("No students found.")
        return
    try:
        update_id = int(input("Enter Student ID to update: "))
        if update_id <=0:
            print("ID should be positive")
            return
    except ValueError:
        print("invalid input")
        return
    found = False
    for student in students:
        if student["student_id"] == update_id:
            student["student_name"] = input("Enter New Name: ").strip().title()
            if student["student_name"] =="":
                print("student should not be empty")
                return
            try:
                student["student_age"] = int(input("enter age :"))
                if student["student_age"] <= 0:
                    print("age should be valid")
                    return 
            except ValueError:
                print("enter valid input")
                return
            student["student_course"] =input ("enter student course:").strip().upper()
            if student["student_course"] == "":
                print("course should not be empty")
                return
            subjects = {}

            for subject in SUBJECTS:
                try:
                    marks = float(input(f"Enter New {subject} Marks: "))

                    if marks < 0 or marks > 100:
                        print("Marks should be between 0 and 100")
                        return

                    subjects[subject] = marks

                except ValueError:
                    print("Invalid input")
                    return

            student["subjects"] = subjects
            save_data(students)
            print("student updated successfully")
            found = True
            break
    if not found:
        print("Student not found.")

def result_card(student):
    subjects = student["subjects"]
    total = sum(subjects.values())
    average = total / len(subjects)
    grade = calculate_grade(average)
    status = pass_fail(average)

    print("\n========== RESULT CARD ==========")
    print("Student ID :", student["student_id"])
    print("Name       :", student["student_name"])
    print("Age        :", student["student_age"])
    print("Course     :", student["student_course"])
    print("-------------------------------")

    for subject, marks in subjects.items():
        print(f"{subject:<12}: {marks}")
    print("-------------------------------")

    print("Total Marks :", total)
    print("Average     :", round(average,2))
    print("Grade       :", grade)
    print("Status      :", status)

    print("===============================")

def remove_student():
    students = load_data()
    if not students:
            print("No students found.")
            return
    try:
        student_id = int(input("Enter Student ID: "))
        if student_id <=0:
            print("ID should be positive")
            return
    except ValueError:
        print("invalid input")
        return
    found = False
    for student in students:
        if student["student_id"] == student_id:
            students.remove(student)
            save_data(students)
            print("student deleted successfully")
            found = True
            break
    if not found:
        print("student for this id not found")

def sort_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    while True:
        print("1. Sort by ID")
        print("2. Sort by Name")
        print("3. Sort by Age")
        print("4. Sort by Marks")
        print("5.return")

        choice = input("Enter your choice: ")
        if choice == "1":
            sorted_students = sorted(students, key=lambda student: student["student_id"])
            for student in sorted_students:
                result_card(student)
        elif choice == "2":
            sorted_students = sorted(students, key=lambda student: student["student_name"])
            for student in sorted_students:
                result_card(student)
            
        elif choice == "3":
            sorted_students = sorted(students, key=lambda student: student["student_age"])
            for student in sorted_students:
                result_card(student)

        elif choice == "4":
            sorted_students = sorted(students,key=lambda student: sum(student["subjects"].values()) / len(student["subjects"]))
            for student in sorted_students:
                result_card(student)

        elif choice =="5":
            break
            
        else:
            print("invalid choice")

def student_statistics():
    students = load_data()
    if not students:
        print("no student found")
        return
    marks = []
    for student in students:
        average = sum(student["subjects"].values()) / len(student["subjects"])
        marks.append(average)

    total_students = len(students)
    total_marks = sum(marks)
    average_marks = total_marks/total_students
    highest_marks = max(marks)    
    lowest_marks = min(marks) 
    for student in students:
        average = sum(student["subjects"].values()) / len(student["subjects"])
        if average == highest_marks:
            print(f"Topper Name : {student['student_name']}")
            break

    for student in students:
        average = sum(student["subjects"].values()) / len(student["subjects"])
        if average == lowest_marks:
            print(f"Lowest Student : {student['student_name']}")
            break

    print("\n===== Student Statistics =====")
    print(f"Total Students : {total_students}")
    print(f"Total Marks    : {total_marks}")
    print(f"Average Marks  : {average_marks:.2f}")
    print(f"Highest Marks  : {highest_marks}")
    print(f"Lowest Marks   : {lowest_marks}") 
            