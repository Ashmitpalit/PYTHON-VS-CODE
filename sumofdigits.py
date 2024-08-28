def sum(x):
    if(x%10==x):
        return x
    else:
        return (x%10)+sum(x//10)
n=int(input("Enter a number:\n"))
print(sum(n))