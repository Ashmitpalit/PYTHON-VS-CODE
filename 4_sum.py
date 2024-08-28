x=int(input("Enter the lower limit "))
y=int(input("Enter the upper limit "))
sum=0
for i in range(x,y+1):
    sum=sum+i
print(f'The sum is = {sum}')