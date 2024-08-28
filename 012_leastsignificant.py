num=int(input("Enter the number "))
if(int(num%10==5)):
    print(int((num%10)**2))
else:
    print(f'Its least significant is {int(num%10)} and not 5')