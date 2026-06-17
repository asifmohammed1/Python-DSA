# # Question 1
# print("Question 1")
# square = lambda a: a*a
# print(square(2))
# print(square(4))
# print(square(5))
#
# # Question 2
# print("Question 2")
# numbers = [1, 2, 3, 4, 5]
# square = lambda x: x*x
# result = map(square,numbers)
# print(list(result))

# Question 3
# print("Question 3")
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even = lambda n: n%2 ==0
# result = filter(even,numbers)
# print(list(result))

# Question 4
# print("Question 4")
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# l1 = lambda x,y: x+y
# result = reduce(l1,numbers)
# print(result)

# Bonus Question
# print("Bonus Question")
#
# from functools import reduce
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = list(filter(lambda x: x%2==0, numbers))
# print("even_num", even_num)
#
# squared_num = lambda a: a*a
# squared_num = list(map(lambda a: a*a, even_num))
# print("squared_num", squared_num)
#
# total_sum = lambda x, y:x+y
# total_sum = reduce(lambda x, y:x+y,squared_num)
# print("total_sum", total_sum)

# Interview question
print("Interview Question")
# Use filter() to keep employees with salary greater than 50000.
# Use map() to extract employee names.
# Use reduce() to calculate total salary
from functools import reduce

employees = [
    {"name": "Asif", "salary": 50000},
    {"name": "Rahul", "salary": 70000},
    {"name": "John", "salary": 40000},
    {"name": "Sara", "salary": 90000}
]

high_salary = list(filter(lambda x: x["salary"]> 50000,employees ))
print("High salary: ",high_salary)

employee_names = list(map(lambda x:x["name"],employees))
print("Employee Names: ",employee_names)

total_salary = reduce(lambda total,x: total + x["salary"],employees,0)
print("Total salary: ",total_salary)






