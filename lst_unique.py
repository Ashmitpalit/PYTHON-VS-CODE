lst=[int(x) for x in input('Enter: ').split()]
unique=[]
for i in lst:
    if (lst.count(i)==1):
        unique.append(i)
if(unique!=[]):
    print('The unique elements: ',unique)
else:
    print('There is no unique element in the list you have inputed')
 