def fun(k,a):
    j=1
    c=0
    while j<len(a):
        if k in a[j]:
            c+=1
        j+=1
    return c

a=input()
a=a.lower()
s=a.split()
k=s[0]
c=[]
cnt=0
for i in k:
    res=fun(i,s)
    if res==len(s)-1:
        cnt+=1
        c.append(i)
print(len(c))