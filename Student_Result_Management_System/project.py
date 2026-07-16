def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"


def add_student():
    print("\n===== ADD STUDENT =====")

    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")

    math = int(input("Enter Maths Marks: "))
    science = int(input("Enter Science Marks: "))
    english = int(input("Enter English Marks: "))

    total = math + science + english
    percentage = total / 3

    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n===== RESULT =====")
    print("Name :", name)
    print("Roll :", roll)
    print("Total :", total)
    print("Percentage :", round(percentage, 2))
    print("Grade :", grade)
    print("Result :", result)
    save_student(name, roll, total, percentage, grade, result)
    print("Student record saved successfully!")

def save_student(name, roll, total, percentage, grade, result):
    file = open("students.txt", "a")

    file.write(f"Name: {name}\n")
    file.write(f"Roll No: {roll}\n")
    file.write(f"Total: {total}\n")
    file.write(f"Percentage: {round(percentage, 2)}%\n")
    file.write(f"Grade: {grade}\n")
    file.write(f"Result: {result}\n")
    file.write("----------------------------\n")

    file.close()

def view_students():
    print("\n===== ALL STUDENTS =====")

    try:
        file = open("students.txt", "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("No student records found.")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    try:
        file = open("students.txt", "r")
        data = file.read()

        if roll in data:
            print("\nStudent Found!\n")
            print(data)
        else:
            print("Student not found!")

        file.close()

    except FileNotFoundError:
        print("No records found.")


def delete_student():
    print("\n===== DELETE STUDENT =====")

    roll = input("Enter Roll Number to Delete: ")

    try:
        file = open("students.txt", "r")
        data = file.readlines()
        file.close()

        file = open("students.txt", "w")

        found = False

        for line in data:
            if roll not in line:
                file.write(line)
            else:
                found = True

        file.close()

        if found:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("No records found.")   
       

while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice! Please try again.")
        