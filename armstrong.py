num=int(input("Enter a number "))
temp=num
sum=0
while(temp!=0):
    ld=temp%10
    sum+=ld**3
    temp//=10

if(sum==num):
    print("It is an Armstrong number ")
else:
    print("It is not a Armstrong number ")