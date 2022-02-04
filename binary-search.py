"""
Created on Mon Jan 31 10:44:31 2022

"""
# mySolution

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

def binarySearch(List, value):
    L = 0
    H = len(List) - 1
    while L<H:
        m = int((L + H) / 2)
        if List[m] == value:
            return m
        elif List[m]<value:
            L = m+1
        elif List[m]>value:
            H = m-1
    return None or -1

print(binarySearch(myList,100))