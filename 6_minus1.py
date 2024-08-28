n=int(input("Enter the first number "))
p=0
ng=0
z=0
while(n!=-1):
    n=int(input("Enter the next number "))
    if(n>0):
        p=p+1
    elif(n<0):
        ng=ng+1
    else:
        z=z+1
print("-1 encountered")
print(f'The number of postive numbers are = {p} and number of negative numbers are = {ng}')