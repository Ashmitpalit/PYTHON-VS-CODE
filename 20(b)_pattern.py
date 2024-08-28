n=int(input("Enter the value of N "))
if(n%2==0):
    r1=n//2
    r2=r1
else:
    r1=(n//2)+1
    r2=n-r1

for i in range(1,r1+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()

for i in range(1,r2+1):
    for j in range(r2,i-1,-1):
        print("* ",end="")
    print()
