n=int(input("Enter the value "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i>=2 and i<n):
            if(j>=2 and j<n):
                print("  ",end="")
            else:
                print("* ",end="")
        else:
            print("* ",end="")
    print()
    print()
