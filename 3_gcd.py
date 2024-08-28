# def gcd(a,b):
#     if(b==0):
#         return a
#     else:
#         return gcd(b,a%b)


# n1=int(input("Enter the first number"))
# n2=int(input("Enter the second number"))
# print(f'GCD of {n1} and {n2} is = {gcd(n1,n2)}')

from math import gcd
n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))
print(f'The GCD of {n1} and {n2} is = {gcd(n1,n2)}')
