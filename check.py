n=int(input())
if(n%2==0):
    print(0)
    if(n>=2 & n<=5):
        print(1)
        print("Weird")
    elif(n>=6 & n<=20):
        print(2)
        print("Weird")
    elif(n>20):
        print(3)
        print("Not Weird")
else:
    print(4)
    print("Weird")