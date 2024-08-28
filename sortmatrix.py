r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))

m=[[int(input())for x in range(c)]for y in range(r)]
f=[]

print("The matrix is")
for i in range(r):
    for j in range(c):
        print(m[i][j],end=" ")
        f.append(m[i][j])
    print()

l=len(f)

for i in range(l-1):
    for j in range(l-i-1):
        if(f[j+1]<f[j]):
            f[j],f[j+1]=f[j+1],f[j]

m1=[]
while(f!=[]):
    m1.append(f[:c])
    f=f[c:]

print("The sorted matrix is")
for i in range(r):
    for j in range(c):
        print(m1[i][j],end=" ")
    print()
