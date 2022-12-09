def fun(n):
    c=0
    a="aeiouAEIOU"
    for i in n:
        if i in a:
            c+=1
    return c
a=input()
l=[]
s=a.split()
for i in s:
    c=fun(i)
    l.append(c)
print(max(l))