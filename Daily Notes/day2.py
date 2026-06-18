# Walrus

name = "teja"

if name:
    print("pass")

# if (name2:= input()) == "teja":
#     print('pass')

# Bitwise

# & | ^ ~ << >>

a = 2
b = 3

print(a & b) # 2 # 2 values 1 consider as 1
print(a | b) # 3 # any one have to be 1
print(a ^ b) # 1 XOR # 2 values has 1 or 0 it consider as 0
print(~a) # -3
print(~b) # -4
print(a << 2) # 8
print(b >> 1) # 1

print(5 << 2) # 24

# 0000101
# 0001010
# 0010100



# lower, upper, strip, split, join, replace, list

a = "hello"
b = "BYE"

c = "   hello world   "

print(a.upper())
print(b.lower())

print(len(c))
c = c.strip()
print(len(c))

l = "apple"
w = "hello world"

n = 124

print(w.split()) # split the words
print(list(l)) # split the letter

sp = w.split()
sp2 = list(l)
print(sp)

j = " ".join(sp)
print(j)

rp = w.replace("world","teja")
print(rp)

# Sting formating

nn = "sony"
age = 30
phone = 123

st = f"hello, {nn} how are you?" # f string
st2 = "hello, good afternoon! {0} {2}".format("teja", age, phone)
st3 = "hello, good moring %s %i" % (nn, phone)

print(st)
print(st2)
print(st3)

