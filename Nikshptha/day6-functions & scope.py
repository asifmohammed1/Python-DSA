# Question 1
print('Question 1')
def calculate_bill(item_name, quantity, price=100):
    total = quantity * price
    return total
print(calculate_bill("Pen", 5, 20))

print(calculate_bill(item_name="Book", quantity=2, price=150))

print(calculate_bill("Pencil", 10))

# Question 2
print('Question 2')
def find_sum(*args):
    return sum(args)

print(find_sum(10, 20))

print(find_sum(1, 2, 3, 4, 5))

print(find_sum(100, 200, 300))

# Question 3
print('Question 3')
def student_info(**kwargs):

    for key, value in kwargs.items():
        print(key, ":", value)
student_info(
    name="Asif",
    age=30,
    city="Warangal")

#Question 4
print('Question 4')
company = "Apple"
def display_company():
    department = "Engineering"

    print(company)
    print(department)
display_company()
print(company)

# Question 5
print("Question 5")
def calculate_area(length: int, breadth: int) -> int:
    """
    Calculates area of rectangle.
    Parameters: length : int
                breadth : int
    Returns:int
    """
    return length * breadth

print(calculate_area(10, 5))
