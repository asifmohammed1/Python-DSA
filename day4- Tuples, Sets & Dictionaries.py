# Question 1
print('Question 1')
fruits = ("apple", "banana", "mango")
print(fruits[0])
print(fruits[-1])

# fruits[1] = "orange" TypeError will appear. Tuple object doesn't support item assignment.

# Question 2
print('Question 2')

student = ("Arun", 30, "Hyderabad")
name, age, city = student
print(name)
print(age)
print(city)

# Question 3
print('Question 3')
numbers = {10, 20, 30}
numbers.add(40)
print(numbers)

# Question 4
print('Question 4')
colors = {"red", "blue", "green"}
colors.remove("blue")
print(colors)

# Question 5
print('Question 5')
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)
print(result)

# Question 6
print('Question 6')

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set1.intersection(set2)
print(result)

# Question 7
print('Question 7')

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
result = set1.difference(set2)
print(result)

# Question 8
print('Question 8')
student = {
    "name": "Ankush",
    "age": 30,
    "city": "Delhi"
}
print(student["name"])
print(student["age"])
student["city"] = "Hyderabad"
print(student)

# Question 9
print('Question 9')
student = {
    "name": "Asif",
    "age": 30,
    "city": "Warangal"
}
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())



