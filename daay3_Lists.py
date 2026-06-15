# Question 1
print('Question 1')

fruits = ["apple", "banana", "mango"]
print(fruits[0])
print(fruits[-1])
fruits[1] = "orange"
print(fruits)

# Question 2
print('Question 2')
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# Question 3
print('Question 3')
colors = ["red", "blue", "green"]
colors.insert(1, "yellow")
print(colors)

# Question 4
print('Question 4')
animals = ["cat", "dog", "rabbit", "dog"]
animals.remove("dog")
print(animals)

# Question 5
print('Question 5')
cities = ["Hyderabad", "Warangal", "Delhi"]
removed_city = cities.pop()
print(removed_city)
print(cities)

# Question 5
print('Question 6')
cities = ["Hyderabad", "Warangal", "Delhi"]
removed_city = cities.pop()
print(removed_city)
print(cities)

# Question 6
print('Question 7')
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)

# Question 7
print('Question 7')
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)

# Question 8
print('Question 8')
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:3])
print(numbers[-3:])
print(numbers[::2])
# =====================================
# Question 9
print("Question 9")
original = [1, 2, 3, 4]
copied = original.copy()
copied.append(5)
print("Original:", original)
print("Copied:", copied)

# Question 10
print("Question 10")

students = [
    ["Asif", 30],
    ["Rahul", 25],
    ["John", 28]
]

print(students[1][1])
print(students[2][0])
students[0][1] = 31
print(students)

