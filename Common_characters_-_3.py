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
j=1
cnt=0
c=[]
for i in k:
    res=fun(i,s)
    
    if res==len(s)-1:
        cnt+=1
        c.append(i)
if cnt==0:
    print(-1)
else:
    c="".join(c)
    print(min(c))