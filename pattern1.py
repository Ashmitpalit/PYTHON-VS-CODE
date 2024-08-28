n=int(input("Enter the number of rows:\n"))

for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    if(i>1):
        for c in range(1,i+1):
            print("*",end="")
    print()
for i in range(1,n):
    for k in range(1,i+1):
        print(" ",end="")
    for j in range(n,i,-1):
        print("*",end="")
    if(i+1!=n):
        for c in range(n,i,-1):
            print("*",end="")
    print()
    

