# Question 1
print(' Question 1')
s = "python developer"
print(s.upper())

# Question 2
print(' Question 2')
name = 'nik'
print(name.upper())

# Question 3
print(' Question 3')
s1 = "Python"
s2 = "PYTHON"

if s1.upper() == s2.upper():
    print("Equal")
else:
    print("Not Equal")

# Question 4
print(' Question 4')
s = "MACHINE LEARNING"
print(s.lower())

# Question 5
print(' Question 5')
s = "Python python PYTHON PyThOn"
print(s.lower().count("python"))

# Question 6
print(' Question 6')
s = "     Python     "
print(s.strip())

# Question 7
print(' Question 7')
username = "   admin   "

if username.strip() == "admin":
    print("Login Successful")
else:
    print("Invalid User")

# Question 8
print(' Question 8')
s = "   Data Science   "
print("Before:", len(s))
print("After:", len(s.strip()))

# Question 9
print(' Question 9')
s = "Python is easy to learn"
print(s.split())

# Question 10
print(' Question 10')
s = "apple,banana,mango,orange"
print(s.split(","))

# Question 11
print(' Question 11')
s = "I love Python programming"
words = s.split()
print(len(words))

# Question 12
print(' Question 12')
name = "Arun Tiwari"
parts = name.split()
print("First Name:", parts[0])
print("Last Name:", parts[1])

# Question 13
print(' Question 13')
lst = ['2026', '06', '15']
print("-".join(lst))

# Question 14
print(' Question 14')
words = ['Python', 'is', 'awesome']
print(" ".join(words))

# Question 15
print(' Question 15')
s = "Python"
print("*".join(s))

# Question 16
print(' Question 16')
s = "I love Java"
print(s.replace("Java", "Python"))

# Question 17
print(' Question 17')
s = "Machine Learning Engineer"
print(s.replace(" ", "_"))

# Question 18
print(' Question 18')
phone = "9876543210"
masked = phone[:3] + "*****" + phone[-2:]
print(masked)

# Question 19
print(' Question 19')
s = "banana"
print(s.replace("a", "@"))

# Question 20
print(' Question 20')
name = "Arun"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Question 21
print(' Question 21')
salary = 50000
print(f"My salary is ₹{salary}")

# Question 22
print(' Question 22')
a = 10
b = 20
print(f"Sum of {a} and {b} is {a+b}")

# Question 23
print(' Question 23')
num = 5
i = 3
print(f"{num} x {i} = {num*i}")

# Question 24
print(' Question 24')
num = 7
print(f"Square of {num} is {num**2}")

# Question 25
print(' Question 25')
name = "Aman"
print("Welcome {}".format(name))

# Question 26
print(' Question 26')
course = "Python"
price = 999
print("{} costs {} rupees".format(course, price))

# Question 27
print(' Question 27')
pi = 3.141592653
print("{:.2f}".format(pi))

# Question 28
print(' Question 28')
marks = 456
total = 500

percentage = (marks / total) * 100
print("Percentage = {:.2f}%".format(percentage))

# Question 29
print(' Question 29')
s = "   PYTHON Programming   "

result = s.strip().lower().replace("programming", "developer")
print(result)

# Question 30
print(' Question 30')
name = "Arushi"
city = "Warangal"
age = 30

print(f"My name is {name}. I am {age} years old and live in {city}.")

# Question 30
print(' Question 31')
name = "Arushi"
city = "Warangal"
age = 30

print(f"My name is {name}. I am {age} years old and live in {city}.")

# Question 32
print(' Question 32')
s = "   Python   "
print(s.strip())
print(s.replace(" ", ""))
print()

# Question 33
print(' Question 33')
s = "Python"
print(s.upper())
print(s.lower())

# Question 34
print(' Question 34')
print("-".join("Python"))

# Question 35
print(' Question 35')
s = "Python"
print("_".join(s))

# Question 36
print(' Question 36')
s = "  Python  "
print(len(s))
print(len(s.strip()))

# Question 37
print(' Question 37')
s = "apple,banana,mango"
print(len(s.split(",")))

# Question 38
print(' Question 38')
name = "nik"
print(f"{name.upper()}")
print()

# Question 39
print(' Question 39')
s = "Python Programming"
print(s.replace(" ", ""))

# Question 40
print(' Question 40')
name = "Aman"
company = "Apple"

print(f"""Hello {name},
Welcome to {company}.
Thank you.""")





