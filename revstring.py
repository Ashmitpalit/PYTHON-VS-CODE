def reverse(st):
    if(len(str)==0):
        return str
    else:
        return reverse(st[1:])+st[0]
    
s=input("Enter a string:\n")
print(reverse(s))