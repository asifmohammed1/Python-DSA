# DAY 1 - VARIABLES & OPERATORS

# Question 1 - Swap Two Numbers
a = 10
b = 20
a, b = b, a
print("Question 1")
print("a =", a)
print("b =", b)

# Question 2 - Temperature Converter
celsius = 37
fahrenheit = (9 / 5 * celsius) + 32
print("Question 2")
print("Fahrenheit =", fahrenheit)

# Question 3 - Reverse 3 Digit Number
num = 123
first = num // 100
middle = (num // 10) % 10
last = num % 10

reverse = last * 100 + middle * 10 + first
print("Question 3")
print("Reverse =", reverse)

# Question 4 - Convert Time to Seconds
hours = 2
minutes = 30
seconds = 15

total_seconds = hours * 3600 + minutes * 60 + seconds
print("Question 4")
print("Total Seconds =", total_seconds)

# Question 5 - Simple Interest
principal = 10000
rate = 8
time = 2

simple_interest = (principal * rate * time) / 100
print("Question 5")
print("Simple Interest =", simple_interest)

# Question 6 - Profit or Loss
cost_price = 500
selling_price = 650

print("Question 6")
if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)
else:
    loss = cost_price - selling_price
    print("Loss =", loss)

# Question 7 - Sum of Digits
num = 456

digit1 = num // 100
digit2 = (num // 10) % 10
digit3 = num % 10
sum_digits = digit1 + digit2 + digit3
print("Question 7")
print("Sum of Digits =", sum_digits)

# Question 8 - Area and Perimeter
length = 10
breadth = 5
area = length * breadth
perimeter = 2 * (length + breadth)
print("Question 8")
print("Area =", area)
print("Perimeter =", perimeter)

# Question 9 - Operators
a = 10
b = 3

print("Question 9")
print("Addition =", a + b)
print("Floor Division =", a // b)
print("Modulus =", a % b)
print("Exponent =", a ** b)

# Question 10 - Salary Breakdown
basic_salary = 50000

hra = basic_salary * 20 / 100
da = basic_salary * 10 / 100
tax = basic_salary * 5 / 100

gross_salary = basic_salary + hra + da
net_salary = gross_salary - tax
print("Question 10")
print("Gross Salary =", gross_salary)
print("Net Salary =", net_salary)

