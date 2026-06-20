print("Hello World"

num = int("abc")

a = 10
b = 0
print(a / b)

numbers = [10, 20, 30]
print(numbers[5])

a = 10
b = 0
if b != 0:
    print(a / b)
else:
    print("Cannot divide by zero")

numbers = [10, 20, 30]
index = 5
if index < len(numbers):
    print(numbers[index])
else:
    print("Invalid Index")

student = {"name": "Asif"}
print(student.get("age","Age Not Found"))

num = input("Enter Number: ")
if num.isdigit():
    num = int(num)
    print(num)
else:
    print("Numbers Only")

# Question 3
try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    result = num1 / num2
except ValueError:
    print("Please Enter Numbers Only")
except ZeroDivisionError:
    print("Cannot Divide By Zero")
except TypeError:
    print("Type Error Occurred")
else:
    print("Result:", result)
    print("Operation Successful")
finally:
    print("Program Ended")

# Question 4
class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("Enter Marks: "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")
    print("Valid Marks")
except InvalidMarksError as e:
    print(e)
except ValueError:
    print("Please Enter Valid Numbers")
    