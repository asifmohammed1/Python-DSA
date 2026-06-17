# Question 1
print("Question 1")
numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = [num for num in numbers if num % 2 == 0]

squares = [num ** 2 for num in numbers if num > 5]
print(even_numbers)
print(squares)

# Question 2
print("Question 2")
numbers = [1,2,3,4,5]
squares = {num: num**2 for num in numbers}
print(squares)

# Question 3
print("Question 3")
table = [
    [
        i * j
        for j in range(1,4)
    ]
    for i in range(1,4)
]
print(table)
