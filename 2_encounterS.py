ch=input("Enter a character ")
l=0
u=0
if(ch.islower()==True):
    l=1
else:
    u=1
while(ch!="S"):
    print("Enter the next character")
    ch=input()
    if(ch.islower()==True):
        l=l+1
        if(ch=='s'):
            ch=chr(83)
            break
    else:
        u=u+1
print("\nS encountered\n")
print(f'Uppercase letters = {u} and Lowercase letters = {l}')