n=input("Enter a binary nunber:\n")
one,zero=0,0
for i in n:
    if(i=='0'):
        zero=zero+1
    else:
        one=one+1
if(zero==1 or one==1):
    print("Yes")
else:
    print("No")
