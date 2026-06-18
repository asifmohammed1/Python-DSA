# Classes

def func1(a):
    return a*2

print(func1(2))

class cl1:
    pass

v = cl1() # object

class cl2:
    def func1(a):
        return a*2
    def func2(b):
        return b-2

c = cl2
print(c.func1(2))
print(c.func2(10))


# Constructor and self

class cl3:
    a = "hello"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        return f"Hello, good morining {self.name}"

    def func2(self, a):
        return f"{a} good morning"

# class variable and instance variable

class cl4:
    a = "hello"
    b = "bye"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func1(self):
        return f"Hello, good morining {self.name}"

    @classmethod
    def func2(cls): # class varibales
        return f"{cls.a} good morning {cls.b}"

t = cl4("sara", 25)
print(t.a)
print(t.name)


# Staticmethod and Classmethod

class cl5:
    a = "teja"

    @classmethod
    def func1(cls):
        return f"Hello {cls.a}"

print(cl5.func1())

class cl6:
    @staticmethod
    def func1(a, b):
        return a+b

print(cl6.func1(2,3))




