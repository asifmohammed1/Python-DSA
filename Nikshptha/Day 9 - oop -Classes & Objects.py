# #Question 1
# print("Question 1")
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
# Student1 = Student("John", 22, "Maths")
# print(Student1.name)
# print(Student1.age)
# print(Student1.course)

# Question 2
# print("Question 2")
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# Employee1 = Employee("Asif", 50000)
# Employee2 = Employee("Rahul", 70000)
#
# print(Employee1.name, Employee1.salary, Employee2.name, Employee2.salary)
# Employee2.salary = 80000
# print(Employee1.name, Employee1.salary, Employee2.name, Employee2.salary)

# Question 3
print("Question 3")
class Employee:
    company = "Google"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Asif", 50000)

emp2 = Employee("Rahul", 70000)

print("Before Change")
print(emp1.name, Employee.company)
print(emp2.name, Employee.company)

Employee.company = "Microsoft"

print("After Change")

print(emp1.name, Employee.company)

print(emp2.name, Employee.company)






