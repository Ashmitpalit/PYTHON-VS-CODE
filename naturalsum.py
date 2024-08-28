def natural(x):
    if(x==1):
        return 1
    else:
        return x+natural(x-1)
n=int(input("Enter the limit:\n"))
print(natural(n))