# Count the chars
s = 'hello good morning'

r = {}
for i in s:
    r[i] = s.count(i)
print(r)

r = {'h': 1, 'e': 1, 'l': 2, 'o': 4, ' ': 2, 'g': 2, 'd': 1, 'm': 1, 'r': 1, 'n': 2, 'i': 1}

for k,v in r.items():
    r[k] = v*2
print(r)

# Find the missing number
l = [1,2,3,4,5,7,8,9,11]
num = 0

for i in l:
    if i !=  num+1:
        print(num+1)
        num += 1
    num += 1

# sort the list

l = [3,1,2,4]
n = 0

l = [1,2,3,4,25,53,34,6,346,34]


for i in range(len(l)):
    for j in range(len(l) - 1):
        if l[j] > l[j + 1]:
            l[j], l[j+1] = l[j+1], l[j]

print(l)
