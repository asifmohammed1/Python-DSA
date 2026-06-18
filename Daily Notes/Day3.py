# List and its methods

l1 = ["asif", "teja", "nishitha", True, 10, 10.5]

print(l1[::-1])

l1[2] = "kumar"

print(l1)

l1.append(False)

print(l1)

l1.insert(1, "Good")

print(l1)

l1.remove("kumar")

print(l1)

l1.pop()

print(l1)

l2 = ["apple", "fish", "banana"]
l3 = [5,2,1,10.5,1.5]
l4 = [True, False]

l4.sort()

print(l4)

l2.reverse()

print(l2)

a = l2 #wrong method
a[1] = 120
print(a)
print(l2)

b = l2.copy()

b[0] = "elephant"
print(b)
print(l2)

n = [
    [1,2,3],
    [True, False],
    [10,10.5,100]
]

print(n)

print(n[1][1])

n[1][1] = True

