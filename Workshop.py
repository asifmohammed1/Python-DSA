
print("hello world")

integer = 22
flaot = 2.5
string = "Samreen"
print(string)
print(string[5])

print(string.upper())
print(string.lower())

print(string[::])

boolen = True , False

list = []
students = ["nik", "2", 2.5, 2.5]

students.append("sana")
print(students)


tuple = ()
roll_num = (1,2)

set = {}
numbers = {1,2,2,3,3,3,4}
print(numbers)

dictionary = {}
student = { "name" : "Nik",
            "age" : 23 }
print(student)

students = "nik", "samreen"
age = 20

print(students)
print(age)


# name = input("Enter a name: ")
# print("Hello", name)

# age = input("Enter my age: ")

a = 2
b = 4
print(a % b)

# comparision operators
# ( ==,  !=, < , >)

a = 100
b = 10
print(a == b)
print(a > b)

# logical operators
# and or not

# if conditions
age = 17
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible")

marks = 46
if marks >= 90:
    print("A")
elif marks >= 60:
    print("B")
elif marks >= 45:
    print("C")
else:
    print("F")

# Loops
print("Hi")

for i in range(0,6):
    print("Hello")
    # 0 -1st index
    # 1 - 2nd index

# for i in range(0,6):
#     print(i)

count = 1
while count <= 5:
    print(count)
    count = count + 1

rain = False
while rain:
    print("TAKE AN UMBRELLA")
    break

# functions

def greet():
    print("Hello N")
greet()

def add(a,b):
    return a + b
print(add(10, 20))


def greet(name):
    print("hello", name)
greet("Rahul")

# OOPS
class Student:
    pass
student1 = Student()

# Encapsulation
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(1000)
account.deposit(500)
account.show_balance()

# Inheritance
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()

# Polymorphism
class Dog:
    def sound(self):
        print("Dog is barking")

class Cat:
    def sound(self):
        print("Cat says meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("insert a key n start")

class Scooty(Vehicle):
    def start(self):
        print("Scooty starts with a key")

car = Car()
scooty = Scooty()

car.start()
scooty.start()
