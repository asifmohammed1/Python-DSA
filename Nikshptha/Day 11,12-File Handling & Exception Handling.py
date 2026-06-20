# Question 1
print("Question 1")
file = open("student.txt", "w")

file.write("Asif\n")
file.write("Rahul\n")
file.write("John\n")

file.close()

file = open("student.txt", "r")

print(file.read())

file.close()

file = open("student.txt", "a")

file.write("Sara\n")

file.close()

print("Updated Contents:")

file = open("student.txt", "r")

print(file.read())

file.close()

# Question 2
print("Question 2")
with open("employees.txt", "w") as file:

    file.writelines(
        [
            "Asif\n",
            "Rahul\n",
            "John\n"
        ]
    )

with open("employees.txt", "r") as file:
    employees = file.readlines()
for employee in employees:
    print(employee.strip())

# Question 3
print("Question 3")
import csv
topper_name = ""
topper_marks = 0

# with open("students.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#
#         print(
#             row["name"],
#             row["marks"]
#         )
#         if int(row["marks"]) > topper_marks:
#
#             topper_marks = int(row["marks"])
#
#             topper_name = row["name"]
# print("Topper:")
# print(topper_name,topper_marks)

# Question 4
print("Question 4")
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid Input")
else:
    print("Result:", result)
    print("Division Successful")
finally:
    print("Program Ended")

# Question 5
print("Question 5")
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be at least 18")
    print("Eligible for Voting")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter numbers only")
except TypeError:
    print("Type Error Occurred")

