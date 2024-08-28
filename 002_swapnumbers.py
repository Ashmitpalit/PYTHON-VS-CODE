def swapping(a,b):
    a=a+b
    b=a-b
    a=a-b
    return (a,b)

n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))
print(swapping(n1,n2))