"""
Created on Tue Feb  1 06:32:43 2022

"""
List1 = [24,78,98, 37,98,101,-2]

# mySolution

# def selectionSort(List):
#     sortedList = []
#     while List:
#         Max = max(List)
#         sortedList.append(Max)
#         List.remove(Max)
    
#     return sortedList
    
# print(selectionSort(List1))




# teacherSolution

def findMax(array):
    max = array[0]
    index_max = 0
    for n in range(1,len(array)):
        if array[n]>max:
            max = array[n]
            index_max = n
    
    return index_max

def selectionSort(array):
    sortedArray = []
    while array:
        index_max = findMax(array)
        sortedArray.append(array.pop(index_max))
    
    return sortedArray

print(selectionSort(List1))