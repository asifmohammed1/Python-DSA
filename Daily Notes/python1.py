# Strings

s = "hello"
print(s[:1:-1])

l = [1,2,4,5]
print(l[::-1])

t = (1,2,4,5)
print(t[::-1])

# s ={1,2,4,5}

d = {"name":"teja", "age": 24}
print(d["age"])

data = [{"name":"teja", "age": 24},{},{}]
data2 = {
        "name":"teja", "age": 24,
         "skills":
             [
             {"cicd": "docker"},{"dev":"python"}
            ]
    }


# Palidrome

import json

a = "1221" # abcba "[1,2,3,2,1]"

# a = json.loads(a)

print(a)
print(a[::-1])

if a == a[::-1]:
    print("Its a Palidrome")
else:
    print("Not a Palidrome")


ss = "[1,2,3,2,1]"
print(list(ss))

import ast

print(ast.literal_eval(ss))
print(json.loads(ss))


# Find the largest number from the list

l = [1,2,3,4,25,53,34,6,346,34]

largestnumber = 0

for i in l:
    if i > largestnumber:
        largestnumber = i
print(largestnumber)

# count vowels

s = "good morning"
vowels = "aeiou"
n = 0
for i in s:
    if i in vowels:
        n += 1
print(n)

# factorial
n = 3 # 3x2x1 = 6
r = 1
for i in range(1, n+1):
    r *= i
print(r)


# fibonacci series

f = 5 # 1

# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 45

f1, f2 = 0,1
for i in range(f):
    f1, f2 = f2, f1+f2
print(f1)

# sum of digits of number
n = 123 # 6
s = 0

n = list(str(n))
nn = []
for i in n:
    nn.append(int(i))
print(sum(nn))


s = 0
for i in n:
    s += int(i)
print(s)


# remove dublicate
l = [1,2,3,4,1,2,3]
l3 = list(set(l))
print(l3)

l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)

# even and odd

l = [1,2,3,4,5,6,7,8,9,10]

for i in l:
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is odd")

# prime number

# prime = 2,3,5,7,11
i = 2

for i in l:
    if i % 2 != 0 and i != 1:
        print(f"{i} is Prime Number")
    elif i == 2:
        print(f"{i} is Prime Number")
    else:
        print(f"{i} is Non Prime Number")

# swep number

a = 100
b = 120

a, b = b,a
