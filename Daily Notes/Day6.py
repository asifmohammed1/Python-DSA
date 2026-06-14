# Functions

def fun1():
    return "Hello"
fun1()

def fun2():
    print("Hello2")
fun2()

def fun3(name):
    return f"Hello {name}"

personname = "teja"
a = fun3(personname)
print(a)

def func4(n, n2):
    return n**n2

# print(func4(4, 3))

a = func4(4,5)
print(a)
b = func4(4,2)
print(b)


def func5(name = "teja"):
    return f"Hello {name}"


def func6(*args):
    return f"Hello {args[0]}"

print(func6("teja","asif","sara"))

def func7(**kwargs):
    return kwargs
    # for k,v in kwargs:
    #     return f"Hello {v}"

print(func7(Name="asif", age=25))

def func8(l):
    return l

ll = [1,2,3,35,4346,43,6,54]
print(func8(ll))


def func9(a,b):
    """
    hello what is this function use for
    """
    return a+b

print(func9(1,2))
print(func9.__doc__)

a = 10

def func10():
    a = 20
    print(a)

func10()
print(a)