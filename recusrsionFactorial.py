"""
Created on Tue Feb  1 08:03:05 2022

"""
def findFactorial(x):
    if x==1:
        return 1
    else:
        return x * findFactorial(x-1)

print(findFactorial(5))
