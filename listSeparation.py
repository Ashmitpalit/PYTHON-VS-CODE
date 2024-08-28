lst=eval(input("Enter the values in the list :\n"))
pos=[]
neg=[]
zero=[]
for i in lst:
    if(lst[i]>0):
        pos.append(lst[i])
    elif(lst[i]<0):
        neg.append(lst[i])
    else:
        zero.append(lst[i])
print("Postive list : ",pos)
print("Negative list : ",neg)
print("Zero list : ",zero)

# lst=eval(input("Enter the values in the list :\n"))
# lst1=[]
# for i in range(len(lst)):
#     if(i>0):
#         lst1.append(lst.pop(lst.index(i)))
# print(lst)
# print(lst1)