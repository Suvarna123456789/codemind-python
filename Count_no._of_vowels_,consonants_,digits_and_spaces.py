n=input()
v=0
c=0
d=0
s=0
vo="aeiouAEIOU"
for i in n:
    if ord(i)==32:
        s+=1
    elif i.isdigit():
        d+=1
    elif i in vo:
        v+=1
    else:
        c+=1
    

print("Vowels:",v)
print("Consonants:",c)
print("Digits:",d)
print("White spaces:",s)
