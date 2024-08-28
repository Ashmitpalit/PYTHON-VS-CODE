opr=input("Enter the operator you want ")
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
if(opr=='+'):
    sum=a+b
    print("The sum is =",sum)

elif(opr=='-'):
    if(a>b):
        diff=a-b
    elif(b>a):
        diff=b-a
    else:
        diff=0
    print("The difference is =",diff)

elif(opr=='*'):
    pro=a*b
    print("The product is =",pro)

elif(opr=='/'):
    div=a/b
    print("The divisor is =",div)

elif(opr=='%'):
    mod=a%b
    print("The remainder is =",mod)

else:
    print("Invalid")