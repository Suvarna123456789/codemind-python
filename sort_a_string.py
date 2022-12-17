l=input()
a=[]
b=[]
for i in range(len(l)):
    if l[i].isalpha():
        a.append(l[i])
    else:
        b.append(i)
a.sort()
for i in b:
    a.insert(i,l[i])
l="".join(a)
print(l)