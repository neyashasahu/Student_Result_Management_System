print("=" * 45)
print("  STUDENT RESULT MANAGEMENT SYSTEM")
print("=" * 45)

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

math = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))

total = math + science + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

print("\n------ RESULT ------")
print("Name :", name)
print("Roll No :", roll)
print("Total Marks :", total)
print("Percentage :", round(percentage, 2), "%")
print("Grade :", grade)

if percentage >= 40:
    print("Result : PASS ✅")
else:
    print("Result : FAIL ❌")

file = open("students.txt", "a")

file.write(f"Name: {name}\n")
file.write(f"Roll No: {roll}\n")
file.write(f"Total: {total}\n")
file.write(f"Percentage: {round(percentage,2)}%\n")
file.write(f"Grade: {grade}\n")

if percentage >= 40:
    file.write("Result: PASS\n")
else:
    file.write("Result: FAIL\n")

file.write("-------------------------\n")
file.close()

print("Student record saved successfully!")