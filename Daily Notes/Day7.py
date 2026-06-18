# Lambda, map, reduce, filter

def func1(a):
    return a*2

print(func1(3))


func2 = lambda a: a*2
print(func2(4))

func3 = lambda a,b: a+b
print(func3(2,3))


# map

l = [1,2,3,4]

def func4(listt):
    l2 = []
    for i in listt:
        l2.append(i*2)
    return l2

print(func4(l))

func5 = list(map(lambda i: i*3, l))

print(func5)


# Filter

l2 = [5,6,7,8,9,1,2]

def func6(listt):
    ll = []
    for i in listt:
        if i%2 == 0:
            ll.append(i)
    return ll

print(func6(l2))

func7 = list(filter(lambda i: i%2 != 0, l2))
print(func7)

# reduce

from functools import reduce
l3 = [1,2,3,4,1,2,4]

# def func8(l3):

func8 = reduce(lambda a,b: a*b, l3)
print(func8)

