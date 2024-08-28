sent=input("Enter a sentence:\n")
f=0
x="abcdefghijklmnopqrstuvwxyz"
for i in x:
    if(i not in sent.lower()):
        f=1
        break
if(f>0):
    print("Not Pangram")
else:
    print("Pangram")