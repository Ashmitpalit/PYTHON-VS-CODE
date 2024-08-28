n=input("Enter the value of n ")
limit=int(input("Enter the limit "))
s=""
sum=0
for i in range(1,limit+1):
    for j in range(1,i+1):
        s=s+n
    sum=sum+int(s)
    s=""
print(sum)
