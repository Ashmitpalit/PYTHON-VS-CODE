def equal(a,b):
    if(a==b):
        return 1
    else:
        return 0

n1=int(input("Enter the first number "))
n2=int(input("Enter the second number "))
if(equal(n1,n2)==1):
    print("Both are equal")
else:
    print("They are not equal")