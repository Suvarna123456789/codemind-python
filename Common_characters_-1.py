def fun(key,a):
    j=1
    c=0
    while j<len(a):
        if key in a[j]:
            c+=1
        j+=1
    return c

a=input()
a=a.lower()
s=a.split()
l=s[0]
j=1
c=[]
cnt=0
for i in l:
    res=fun(i,s)
    if res==len(s)-1:
        cnt+=1
        c.append(i)
if cnt==0:
    print(-1)
else:
    c="".join(c)
    print(c)