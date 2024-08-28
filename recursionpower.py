def power(n,p):
    if(p==1):
        return n
    else:
        return n*power(n,p-1)
x=int(input("Enter your nunber:\n"))
p=int(input("Enter the power:\n"))
print(power(x,p))