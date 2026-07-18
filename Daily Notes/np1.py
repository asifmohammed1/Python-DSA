#numpy
import numpy as np

l = [1,2,3,4,5]
print(type(l))

arr = np.array(l)
print(type(arr))


a = [1,2,3,4] # (4,0)
b = [[1,2,3],[4,5,6]] # (2,3)
c = [[[1,2],[1,2]], [[1,2],[1,2]]] # (2,2,2)

arr1 = np.array(a)
arr2 = np.array(b)
arr3 = np.array(c)

arr1.shape
arr1.min()
arr1.dtype

arr1[::-1] #slicing

w = np.arange(1,7) # creates a np from 1 to 6
w.reshape(1,1,3,2)

a = np.array([1,2,3])
b = np.array([4,5,6])

# a+b = [5,7,9]

arr1[arr1 > 2]

q = np.random.randint(1,10,5)

