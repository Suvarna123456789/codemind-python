a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
for i in a:
    if i in b and i.isalpha() and i not in c:
        c.append(i)
for i in b:
    if i in a and i.isalpha() and i not in c:
        c.append(i)
print(len(c))