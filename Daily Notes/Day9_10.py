# Class part 2
from cgi import print_environ_usage


# Inheritances

class cl1:
    def func1():
        return "hello"

class cl11:
    def func11():
        return "hello 111"

class cl2(cl1, cl11):
    def func2():
        return "bye"

print(cl1.func1())
print(cl2.func1())
print(cl2.func2())


class m1:
    def func1():
        return "step 1"

class m2(m1):
    def func2():
        return "step 2"

class m3(m2):
    def func3():
        return "step 3"

print(m1.func1())
print(m2.func1())
print(m2.func2())
print(m3.func1())
print(m3.func2())
print(m3.func3())

# polymorephism, method override

class cl1:
    def func1(a,b):
        c = a*b
        return c

class cl2(cl1):
    def func1(a,b):
        c = a-b
        return c
class cl3(cl1):
    def func1(a,b):
        return "hello cl3"
class cl4(cl1):
    def func1(a,b):
        return "hello cl4"

print(cl2.func1(2,3))

# Encapsulation - Public, protected, private

class pub:
    def __init__(self):
        self.name = "public teja"

print(pub().name)

class pro:
    def __init__(self):
        self._name = "protected teja"

print(pro()._name)

class private:
    def __init__(self):
        self.__name = "protected teja"

# print(private().__name)

# __str__, __repr__, __len__, __eq__

class strcl:
    def __str__(self):
        return "Hello good morning"

print(strcl())

class reprcl:
    def __repr__(self):
        return "morning('hello')"

print(reprcl())

class lencl:
    def __len__(self):
        return 5

print(len(lencl()))

class eqcl:
    def __init__(self, age):
        self.age = age

    def __eq__(self,age2):
        return self.age == age2.age

eq1 = eqcl(20)
eq2 = eqcl(20)
print(eq1 == eq2)