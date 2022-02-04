"""
Created on Tue Feb  1 19:50:12 2022

"""
def arraySum(array):
    if len(array) == 0:
        return 0

    return array[0]+ arraySum(array[1:])

q1 = [44,1,2,3]
print(arraySum(q1))
