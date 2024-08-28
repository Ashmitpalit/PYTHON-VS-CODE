# def digits(x):
#     c=0
#     while(x!=0):
#         c=c+1
#         x//=10

# def checkAutomorphic(n):
#     sq=n**2
#     d=digits(n)
#     if(sq%pow(10,d)==n):
#         print("Automorphic Number")
#     else:
#         print("Not an Automorphic number")


# num=int(input("Enter a number\n"))
# checkAutomorphic(num)



num3 = int(input('enter number: '))
a = str(num3)

sq2 = num3 ** 2
b= str(sq2)

if b.endswith(a):
    print('ok')
else:
    print('NOT OK')
#this is working