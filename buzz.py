def buzz(x):
    if((x%7==0) or (x%10==7)):
        print("It is a Buzz number")
    else:
        print("It is not a Buzz number")

num=int(input("Enter a number\n"))
buzz(num)