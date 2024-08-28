# f=open("Text.txt","r")
# v=["a","e","i","o","u"]
# x=""
# c=0
# l=0
# w=0
# if(f.read!=None):
#     for i in f.read():
#         if(i=="\n"):
#             l=l+1
#     print(l+1)
# f.close()

f=open("Text.txt","w")
f.writelines("Hello My name is Ashmit Palit")
f.close()