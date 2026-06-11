# DAY 2 - STRINGS & OPERATORS

# Question 1
s = "PYTHONPROGRAMMING"
print('Question 1')
print(s[:6])
print(s[6:])
print(s[:6][::-1])
print(s[6:][::-1])

# Question 2
s = "ABCDEFGHIJKL"
print('Question 2')
print(s[::2])
print(s[1::2])

# Question 3
print('Question 3')
s = "DataScience"
print(s[::-1])

# Question 4
print('Question 4')
s = "ArtificialIntelligence"
print(s[:10])
print(s[10:])

# Question 5
print('Question 5')
s = "PythonDeveloper"
print(s[::3])

# Question 6
print('Question 6')
s = "0123456789"
print(s[::-2])
print(s[-2::-2])

# Question 7
print('Question 7')
s = "MachineLearning"
print(s[7:8])

# Question 8
print('Question 8')
s = 'Programming'
s1=(s[1:4][::-1])
s2=(s[:])
print(s1 + s2)

# Question 9
print('Question 9')
s = "Python"
print(s[0] + s[1] * 2 + s[2] * 3 + s[3] * 4 + s[4] * 5 + s[5] * 6)

# Question 10
print('Question 10')
s = "OpenAI"
print(s[::-1])

# Question 11
print('Question 11')
a = 10
b = 10.0
print(a == b)
print(type(a) == type(b))

# Question 12
print('Question 12')
a = True
b = False
print(a + b)
print(a * 10)

# Question 13
print('Question 13')
x = 5
y = 5.0
print(id(x) == id(y))

# Question 14
print('Question 14')
x = (1)
y = (1,)
z = [1]
print(type(x))
print(type(y))
print(type(z))

# Question 15
print('Question 15')
print(bool(""))
print(bool(" "))
print(bool(0))
print(bool(-1))

# Question 16
print('Question 16')
print(True and False or True)

# Question 17
print('Question 17')
x = 10
print(x > 5 and x < 20)
print(x > 5 and x > 20)

# Question 18
print('Question 18')
print(not False and True)
print(not (False and True))

# Question 19
print('Question 19')
a = 0
b = 5
print(a and b)
print(a or b)

# Question 20
print('Question 20')
print(5 > 2 and 10 > 20 or 30 > 10)

# Question 21
print('Question 21')
a = 5
a += 10
print(a)

# Question 22
print('Question 22')
a = 5
a *= 3
a += 2
a //= 4
print(a)

# Question 23
print('Question 23')
x = 100
x %= 7
print(x)

# Question 24
print('Question 24')
a = 2
a **= 4
print(a)

# Question 25
print('Question 25')
a = 50

a += 10
a -= 5
a *= 2
a /= 5
print(a)

# Question 26
print('Question 26')
print(10 == 10.0)
print(10 is 10.0)

# Question 27
print('Question 27')
print("apple" > "Apple")

# Question 28
print('Question 28')
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] is [1, 2, 3])

# Question 29
print('Question 29')
a = None
print(a == None)
print(a is None)

# Question 30
print('Question 30')
print(5 != 5)
print(5 >= 5)
print(5 <= 4)

# Question 31
print('Question 31')
s = "Python"
print(s[::-2])

# Question 32
print('Question 32')
a = True
b = False
print((a or b) and (not b))

# Question 34
print('Question 34')
print(type({}))
print(type(()))
print(type([]))

# Question 35
print('Question 35')
s = "ABCDEFGHIJ"
print(s[::-2])

# Question 36
print('Question 36')
s = "Python"
print(s[-1:])

# Question 37

s = 'Pythonisacodinglanguage'
print(s[::2][::-1])


# Question 38
print('Question 38')
a = [1, 2]
b = [1, 2]
print(a == b)
print(a is b)

print(10 == 10.0)
print(10 is 10.0)

print(None is None)
print(None == None)

# Question 39
print('Question 39')
print(bool("False"))

# Question 40
print('Question 40')
a = 10
b = 20
a, b = b, a
print(a)
print(b)


