bin=input("Enter any binary number")
x=bin.index(".")
d=bin[0:x]
dd=bin[x+1:]
l1=len(d)
l2=len(dd)
sum1=0
sum2=0
c=0
c2=-1
while(l1!=0):
    sum1=sum1+((2**c)* int(d[l1-1]))
    c=c+1
    l1=l1-1

for i in range(0,l2):
    sum2=sum2+((2**c2)*int(dd[i]))
    c2=c2-1

dec=sum1+sum2
print(f'The decimal equivalent of {bin} is {dec}')
