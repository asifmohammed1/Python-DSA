# File handling : read(r), write(w), append(a), read+write(r+)

path = "test.txt"

readfile = open(path, "r")
content = readfile.read()
print(content)
readfile.close()

readfile = open(path, "w")
writecontent = readfile.write("bye")
readfile.close()

readfile = open(path, "a")
appendcontent = readfile.write("\nhello teja")
readfile.close()

with open("test.txt") as file:
    content = file.readlines()

with open("test.txt", "a") as file:
    content = file.writelines("\nnew words")

import csv
with open("test.csv", "r") as file:
    read = csv.reader(file)
    for i in read:
        print(i)

print("Exception handling")
# try/except

try:
    a = "teja"
    if 10 in a:
        print("pass")
    else:
        print("fail")
except:
    print("Pleae check the code")

# try/except/else/finally

try:
    b = 10/2
except:
    print("check the code")
else:
    print("sucess")
finally:
    print("Always runs")


try:
    10/0
except (ValueError,FileExistsError, ModuleNotFoundError, ZeroDivisionError, SyntaxError) as e:
    print(e)

print("hello")