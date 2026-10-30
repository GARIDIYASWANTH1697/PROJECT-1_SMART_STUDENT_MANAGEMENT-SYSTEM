from student import Add_student, show_students,search_student,update_student,remove_student,student_statistics,sort_students

while True:
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Student Statistics")
    print("7. Sort Students")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        Add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()

    elif choice == "5":
        remove_student()

    elif choice == "6":
        student_statistics()
    elif choice == "7":
        sort_students()

    elif choice == "8":
        print("Thank You")
        break
    else:
        print("invalid input")
    
        