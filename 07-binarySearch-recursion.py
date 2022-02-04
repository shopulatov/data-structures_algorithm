"""
Created on Tue Feb  1 20:33:24 2022

"""
def binarySearch(array, value, start = 0, finish = None):
    if finish == None:
        finish = len(array)-1
    if start>finish:
        return None
    
    mid = (start+finish)//2
    if value == array[mid]:
        return mid
    elif array[mid]<value:
        return binarySearch(array, value, mid+1,finish)
    else:
        return binarySearch(array, value, start, mid-1) 
    return None

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]
print(binarySearch(myList,990))