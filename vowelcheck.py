vowel=["a","e","i","o","u"]
found=[]
word=input("Enter the word whther the vowels needs to be traced\n")
word=word.lower()
for i in word:
    if i in vowel:
        if i not in found:
            found.append(i)
found.sort()
print(found)