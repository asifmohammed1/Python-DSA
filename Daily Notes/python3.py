# getter setter
# decoraters

class Test:
    def __init__(self, name):
        self.name = name

    def func1(self):
        return "hello"

    def func2(self):
        return "bye"

obj = Test("teja")
print(obj.func1())

# Getter and setter

class Test2:
    def __init__(self, name):
        self.name = name

    # getter method
    def get_name(self):
        return self.name

    # setter (set the new name)
    def set_name(self, name):
        if type(name) == str:
            self.name = name
            return self.name
        else:
            return "invalide"

obj2 = Test2("sara")
print(obj2.get_name())
print(obj2.set_name("nik"))
print(obj2.get_name())


print("******decoraters********")

def func1(sample):
    def func2():
        print("before fun")
        sample()
        print("secound (inside func1)")
        # return "func2 completed"
    return func2

@func1
def sample():
    print("sample func")

ob = sample()
print(ob)

# pandas(2 days), sql (4 days), fastapi (2 days) and DSA (3 days)
