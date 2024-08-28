r=int(input("Enter the number of rows"))
c=int(input("Enter the number of columns"))

m=[[int(input())for x in range(c)]for y in range(r)]

print("The matrix is ")
for i in range(r):
    for j in range(c):
        print(m[i][j],end=" ")
    print()

t=[]
for i in range(r):
    f=[]
    for j in range(c):
        f.append(m[j][i])
    t.append(f)

for i in range(c):
    for j in range(r):
        print(t[i][j],end=" ")
    print()