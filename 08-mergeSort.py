"""
Created on Wed Feb  2 09:19:56 2022

"""
def mergeSort(array):
    if len(array)>1:
        
        m = len(array)//2
        right = array[m:]
        left = array[:m]
        
        mergeSort(right)
        mergeSort(left)
        
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            
        while i<len(left):
            array[k] = left[i]
            i += 1
            k += 1
        
        while j<len(right):
            array[k] = right[j]
            j += 1
            k += 1
        

a = [6,7,8,2,3,1,0,-2,-46,37]
mergeSort(a)
print(a)