def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
x=int(input("Enter the number of terms:\n"))
print(fibo(x))
