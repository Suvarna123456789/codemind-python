def fun(n):
    v="aeiouAEIOU"
    c=0
    for i in range(0,len(n)):
        if n[i] in v:
            c+=1
    return c
a=input()
l=[]
s=a.split()
for i in s:
    c=fun(i)
    l.append(c)
if len(l)==1:
    print(1)
else:
    print(l.count(max(l)))