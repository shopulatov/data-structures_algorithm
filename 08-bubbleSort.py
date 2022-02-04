"""
Created on Wed Feb  2 08:37:51 2022

"""
def bubbleSort(array):
    n = len(array)
    for j in range(n-1):
        for i in range(n-1):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
     

a=[8,2,4,5]
bubbleSort(a)
print(a)