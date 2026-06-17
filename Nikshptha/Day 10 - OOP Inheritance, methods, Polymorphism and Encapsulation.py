# Question 1
class Employee:

    company = "Google"

    def __init__(self, name):
        self.name = name

    def display_employee(self):
        print("Employee:", self.name)

    @classmethod
    def display_company(cls):
        print("Company:", cls.company)

    @staticmethod
    def calculate_bonus(salary):
        return salary * 0.10

emp = Employee("Asif")

emp.display_employee()

Employee.display_company()

print( "Bonus:",Employee.calculate_bonus(50000))

# Question 2
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):

    def __init__(self, name, age, salary):

        super().__init__(name, age)

        self.salary = salary

    def display(self):

        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

emp = Employee( "Asif", 30,50000)
emp.display()

# Question 3
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Bark")

class Puppy(Dog):

    def sound(self):
        print("Puppy Bark")

puppy = Puppy()
puppy.sound()
animal = Animal()
animal.sound()

# Question 4
class Book:

    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

book1 = Book(
    "Python Basics",
    200
)
book2 = Book("Advanced Python",200)
print(book1)

print(repr(book1))

print(len(book1))

print(book1 == book2)

# Question 5
class BankAccount:

    def __init__(self, balance):

        self.__balance = balance

    def deposit(self, amount):

        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print("Withdraw Successful")

        else:

            print("Insufficient Balance")

    def get_balance(self):

        return self.__balance

class SavingsAccount(BankAccount):

    def withdraw(self, amount):

        if self.get_balance() - amount >= 1000:

            print("Withdraw Successful")

        else:

            print("Minimum Balance Required")

acc1 = BankAccount(10000)

acc2 = SavingsAccount(5000)

acc1.withdraw(500)

acc2.withdraw(5000)