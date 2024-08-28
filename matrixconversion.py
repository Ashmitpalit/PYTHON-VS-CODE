n=int(input("Enter number of rows: "))

# m=[]
# print("Enter the elements in the matrix")
# for i in range(0,n):
#     x=[]
#     for j in range(0,n):
#         x.append(int(input()))
#     m.append(x)

m=[[int(input()) for x in range(n)] for y in range(n)]

print("The matrix is:")
for i in range(0,n):
    for j in range(0,n):
        print(m[i][j],end="   ")
    print()

for i in range(0,n):
    for j in range(0,n):
        if(i<j):
            m[i][j]=0  

print("The new matrix is:")
for i in range(0,n):
    for j in range(0,n):
        print(m[i][j],end="  ")
    print()