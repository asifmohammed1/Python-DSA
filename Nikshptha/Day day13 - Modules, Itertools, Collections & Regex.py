# Question 1
print("Question 1")
# Method 1
import math
print(math.sqrt(25))
print(math.pi)

# Method 2
from math import sqrt, pi
print(sqrt(25))
print(pi)

# Method 3
import math as m
print(m.sqrt(25))
print(m.pi)

# Question 2
print("Question 2")
import os
import sys
import math
import random

print("Current Directory:")
print(os.getcwd())

print("Python Version:")
print(sys.version)

print(math.factorial(5))

print("Random Number:")
print(random.randint(1, 10))

# Question 3
print("Question 3")
from itertools import combinations
from itertools import permutations
from itertools import product

# Question 4
print("Question 4")
letters = ["A", "B", "C"]
print(list(combinations(letters, 2)))
print(list(permutations(letters, 2)))
print(list(product([1, 2],["A", "B"])))

# a
from collections import Counter
words = [
    "python",
    "java",
    "python",
    "c++",
    "java",
    "python"]
result = Counter(words)
print(result)
# b
from collections import defaultdict
students = [
    ("Asif", "Warangal"),
    ("Rahul", "Hyderabad"),
    ("John", "Warangal")]

cities = defaultdict(list)
for name, city in students:
    cities[city].append(name)
print(dict(cities))

# Question 5
print("Question 5")
import re
text = """
Asif scored 95 marks.
Rahul scored 80 marks.
Call: 9876543210
Email: asif@gmail.com
"""
email = re.search(r"\w+@\w+\.\w+",text)
print(email.group())
new_text = re.sub(r"\d","*",text)
print(new_text)
result = re.split(r"\s+",text)
print(result)
