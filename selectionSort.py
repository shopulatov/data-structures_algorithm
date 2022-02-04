"""
Created on Wed Feb  2 23:37:39 2022

"""
def selectionSort(array):
    n = len(array)
    
    for i in range(n):
        min = i
        for j in range(i+1,n):   
            if array[j] < array[min]:
                min = j
                
        array[i], array[min] = array[min], array[i]
        
    return array

a = [8,4,5,3,2,9,1,5]
print(selectionSort(a))