a=input()
b=input()
a=a.lower()
b=b.lower()
c=[]
for i in a:
    if i in b and i not in c and i.isalpha():
        c.append(i)
if len(c)==0:
    print(-1)
else:
    c.sort()
    c="".join(c)
    print(c)