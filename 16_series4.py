n=int(input("Enter the value "))
sum=0
for i in range(1,n+1):
    sum=sum+((i*i)/i)
print(f'Answer = {sum}')