def fun1(name):
    print(f"Hello {name}")

fun1("asif")

def func2(name):
    return f"Hello {name}"

a = func2("nik")
print(a)
print(func2("teja"))

def func3(name="nik"):
    return f"good mrng {name}"

print(func3(name="sara"))

def func4(*args):
    return args[0]

print(func4("asif","nik","sara"))

def func5(**kwargs):
    print(type(kwargs))
    return kwargs["name"]

print(func5(name="nik",age=20,phone=123))