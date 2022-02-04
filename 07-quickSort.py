"""
Created on Tue Feb  1 21:23:44 2022

"""
from random import randrange
def quickSort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array.pop(randrange(len(array)))
        less = [i for i in array if i<=pivot]
        more = [i for i in array if i>pivot]
        return quickSort(less)+[pivot]+quickSort(more)

a = [1,-4,5,2,3,7,8,8,9,4,5,2]
print(quickSort(a))