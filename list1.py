n=int(input("Enter the number of elements in the list "))

l=[]
# for i in range(0,n):
#     element=int(input())
#     l.append(element)

# print("The list is \n",l)
# sum=0
# for i in range(0,n):
#     sum+=l[i]
# print("The sum is =",sum)

l1=list(map(int,input().strip().split()))[:n]
print(l1)

revlist=l[::-1]
print(revlist)