
a = "teja"
a1 = "1234"
a3 = 'teja1'

b = 41
b1= "23" #str
b2 = int(b1) #int

c = 41.0
c2 = "481.0"
c3 = float(c2)
c4 = float(b2) #float

a4 = str(b)

d = True
d2 = False

print("test")

print(type(a))

f=g=h = "apple"

t,y,u = 1,2,3

print(f)
print(h)
print(y)

x = 14j


# Datatypes

# list, tuple, set, dict (object)

l1 = [1, "teja", 10.2]
l2 = [1,2,3,4]

t1 = (1, 'teja', 10.2)
t2 = (1,2,3,4)

s1 = {1,2,3,4,5}


d1 = {"name":"teja", "age":20, a:"123"}

print(type(d1))

# single line comment

# 123
# 123
# 123

strval = "hello how are you"

# True = "124"

print(strval[1:])
print(strval[1:7:2])

print(strval[-7:-1])
print(strval[-7:-1:2])

inputval = input("enter input value :")

print(type(inputval))

strvalC = strval.upper()

print(strvalC)

w = "hello 123   "

print(len(w))
print(len(w.strip()))

print(w.count("l"))

# Operaters

p = 2
q = 3

q2 = p**3




if p<=2:
    print("hello")
else:
    pass

if p<2 :  print("hello")

if (b:= 40) < 50:
    print("good") #walrus

if b > 20 and b > 50:
    print('ok')

if not b > 20:
    print("pass")
else:
    print("fail")
