# Conditionals & Loops
from itertools import count

# if, elif, else

Marks = int(input("Input your marks :"))

if Marks == 100:
    print("Full Marks")
elif Marks < 100 and Marks >= 60:
    print("Grade A")
elif Marks < 60 and Marks >= 35:
    print("Grade B")
elif Marks < 35:
    print("Fail")
else:
    print("Invaild")

data = [{"Name": "a", "Age": 21, "Number": 124, "Address": "Mumbai", "Skills": "Python"},
        {"Name": "a", "Age": 30, "Number": 12312312, "Address": "Mumbai2", "Skills": "Python2"},
        {"Name": "b", "Age": 25, "Number": 456, "Address": "Goa", "Skills": "Java"},
        {"Name": "c", "Age": 30, "Number": 789, "Address": "Hyderbad", "Skills": "c lang"}]


for i in data:
    if i["Name"] == "a":
        print("pass1")
        if i['Age'] < 30:
            print(f"Name: {i['Name']} has age {i['Age']}")
        else:
            print(f"Name: {i['Name']} has age not satified {i['Age']}")
    else:
        pass


# for loop, while loop.


f = ["apple", "manago", 10, True, 25.5]

for i in f:
    if i == "apple":
        print("this this apple")
    else:
        pass

for i in range(0, 5):
    print(i)

for index,value in enumerate(f):
    print(f"Index number {index}: {value}")

# While loop.

for i in range(5):
    print(i)

i = 0
while i < 10:
    print(i)
    i += 1

password = ""
while password != "admin":
    password = input("Enter password :")

print("Login success")

# break and continue

c = 0
while c < 10:
    c += 1
    if c == 8:
        break
    if c == 3:
        continue

    print(c)


# Nest loop

nss = [[1,2,3],[7,8,9],[4,5,6]]
nss2 = ["apple", "teja"]

for i in nss:
    print(i)
    for j in i:
        print(j)

for i in nss2:
    print(i)
    for j in i:
        print(j)

l10 = [1,2,3,4,5]

listt = []
for i in range(10):
    if i > 5:
        listt.append(i)
    else:
        listt.append(i*2)

print(listt)


lc = [i*2 for i in range(20) if i < 10 ] # list comprohenstion

print(lc)

n = int(input("Enter number :")) # 10
for i in range(n):
    if i%2 == 0:
        print(f"Number {i} : Even")
    else:
        print(f"Number {i} : Odd")

sum = int(input()) # 10
for i in range(sum):
    print(i**2)

# dict comp

d = {"name":"teja", "age":20}

for k,v in d.items():
    if k == "name":
        print({k:v})

a = {k:v for k,v in d.items() if k == "name"}

print(a)