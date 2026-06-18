# Tuple

t = (10,20,40,10,20,20)

print(t[1])

print(type(t))

a,b,c = (10,20.4,True)

print(type(c))

print(t.count(10))
print(t.index(20))


# Set

s = {1,1,2,3,4,5}

print(s)

print(set(t))

s.add(6)

print(s)

s.remove(2)

print(s)

s.discard(100)
print(s)

s.pop()
print(s)

s1 = {1,2,3}
s2 = {5,2,3}

s3 = s1 | s2
s4 = s1 & s2
s5 = s2 - s1
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)