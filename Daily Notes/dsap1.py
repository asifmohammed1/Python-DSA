# 1. Largest number from array

l = [1,5,2,3,7,4] #o/p - 7
print(max(l))

# largest = 0
#
# for num in l:
#     if num > largest:
#         largest = num
#
# print(largest)

def find_largest_num(parameterslist):
    largest = 0
    for num in parameterslist:
        if num > largest:
            largest = num
    return largest

print(find_largest_num(l))

# 2. Reverse an array

l = [1,5,2,3,7,4]

def reverse_array(parlist):
    return parlist[::-1]
print(reverse_array(l))

def reverse_array2(parlist):
    ra = []
    for i in parlist:
        ra.insert(0, i)
    return ra

print(reverse_array2(l))

# 3. Check Palindrome

s = "abcba"
