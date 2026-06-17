# Question 1
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_result(self):

        total = sum(self.marks)

        average = total / len(self.marks)

        if average >= 90:
            grade = "A"

        elif average >= 75:
            grade = "B"

        elif average >= 60:
            grade = "C"

        elif average >= 40:
            grade = "D"

        else:
            grade = "Fail"

        result = {
            "name": self.name,
            "total": total,
            "average": average,
            "grade": grade
        }

        print("Name:", result["name"])
        print("Total:", result["total"])
        print("Average:", result["average"])
        print("Grade:", result["grade"])


student = Student(
    "Asif",
    [90, 80, 85, 95, 88]
)

student.calculate_result()

# Question 2
print("Question 2")
class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 20/100
        da = self.basic_salary * 10/100

        gross_salary = (self.basic_salary + hra + da)

        details = {
            "name": self.name,
            "basic_salary": self.basic_salary,
            "gross_salary": gross_salary
        }

        return details

employees = [
    Employee("Asif", 50000),
    Employee("Rahul", 80000)
]

for emp in employees:

    data = emp.calculate_salary()

    print(
        data["name"],
        "->",
        data["gross_salary"]
    )

    if data["gross_salary"] > 70000:
        print("High Salary")

# Question 3
print("Question 3")
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def inventory_value(self):
        return self.price * self.quantity

products = [
    Product("Laptop", 50000, 5),
    Product("Mouse", 500, 20)
]

for product in products:
    data = product.inventory_value()
    print(product.name)

    print( "Inventory Value:",product.inventory_value())

    if product.quantity < 10:
        print("Low Stock")

# Question 4
print("Question 4")
class Library:

    def __init__(self):

        self.books = {
            "Python": 5,
            "Java": 2,
            "C++": 0
        }

    def add_book(self, book, quantity):

        self.books[book] = quantity

    def borrow_book(self, book):

        if self.books.get(book, 0) > 0:

            self.books[book] -= 1

            print(book, "borrowed successfully.")

        else:

            print(book, "is Out of Stock.")

    def display_books(self):

        for book, qty in self.books.items():

            print(book, ":", qty)

library = Library()

library.borrow_book("Python")

library.borrow_book("C++")
library.add_book("Java",2)

library.display_books()

# Ultimate Challenge
class School:

    def __init__(self):

        self.students = []

    def add_student(self, name, marks):

        student = {
            "name": name,
            "marks": marks
        }

        self.students.append(student)

    def display_students(self):

        for student in self.students:

            print(
                student["name"],
                "-",
                student["marks"]
            )

    def topper(self):

        top_student = self.students[0]

        for student in self.students:

            if student["marks"] > top_student["marks"]:

                top_student = student

        return top_student

school = School()

school.add_student("Asif", 95)

school.add_student("Rahul", 80)

school.add_student("John", 90)

print("Students:")

school.display_students()

topper = school.topper()

print("Topper:", topper["name"])

print("Marks:", topper["marks"])