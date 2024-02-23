from array import *
arr1 = array('i', [1,2,4,5,6,7,8])
arr2 = array('d', [1,256,456,45,6,7,8])

# insert?
arr1.insert(5,10)
print(arr1)

# traversal?
def traversal_Array(array):
    for i in array:
        print(i)
traversal_Array(arr2)

# access element?
def accessElement(array, index):
    if index >= len(array):
        print("there is none!!")
    else:
        print(array[index])
accessElement(arr1, 3)

# searching element?
def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "does not exist"
print(searchInArray(arr1, 4))

# Two dimensional array
# a - 1,34,54,34
# b - 3,65,45,3
# c - 4,54,54,4
import numpy as np
twoDarray = np.array([[1,34,54,34], [3,65,45,3], [4,54,54,4]])
print(twoDarray)

# transverse?
def transverseTDarray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
transverseTDarray(twoDarray)
''' you can do this without numpy'''
