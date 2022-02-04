"""
Created on Tue Feb  1 19:18:30 2022

"""
def find_gcd(a,b):
    n1 = max(a,b)
    n2 = min(a,b)
    if n1 % n2 == 0:
        return n2
    else:
        rem = n1 % n2
        return find_gcd(n2, rem)

a = find_gcd(168, 64)
print(a)