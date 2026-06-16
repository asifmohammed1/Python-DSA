# Question 1
print("Question 1")
n = int(input('enter marks: '))
if n>90 & n<100:
    print("Grade A")
elif n>75 & n<89:
    print("Grade B")
elif 60>n<74:
    print("Grade C")
elif 40>n<59:
    print("Grade D")
else:
    print("Fail")

# #Question 2
print('Question 2')
for i in range(1,11):
    print(i)

fruits = ["apple", "banana", "mango", "orange"]
for index, fruit in enumerate(fruits):
    print(index,fruit)

# Question 3
print("Question 3")
while n!=0:
    n = int(input("Enter a number: "))
    if n<0:
        continue
    else:
        print(n*n)

#Question 4
print('Question 4')
for i in range(2, 11):
    for j in range(2, i):
        if i % j == 0:
            print(i,"is not prime")
            break
    else:
        print(i, "is prime")

# Bonus Question
n=0
while n!=4:
    print("1. Print Numbers\n 2. Print Even Numbers\n 3. Print Multiplication Table\n 4. Exit")
    n = int(input("Enter choice: "))
    if n==1:
        print("1. Print Numbers")
        m=int(input("Enter number: "))
        for i in range(0,m+1):
            print(i)
    elif n==2:
        print("2. Print Even Numbers")
        o=int(input("Enter number: "))
        for i in range(1,o+1):
            if i%2==0:
                print(i)
    elif n==3:
        print("3. Print Multiplication Table")
        p=int(input("Enter number: "))
        for i in range(1,11):
            print(f"{p} * {i} = {p*i}")
    else:
        print("Invalid Input")