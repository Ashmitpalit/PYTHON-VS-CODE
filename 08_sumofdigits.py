num=int(input("Enter a number "))
temp=num
sum=0
while(num!=0):
    sum=sum+int((num%10))
    num=num/10
print(f'Sum of the digits of {temp} is {sum}')
