n=input()
a=[]
c=0
for i in n:
    if i.isdigit():
        a.append(i)
for i in a:
    c+=int(i)
print(c)