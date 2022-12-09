def fun(a):
    v="aeiouAEIOU"
    i=0
    cnt=0
    j=-1
    while i<=len(a)//2 and j>=-(len(a))//2:
        if (a[i] in v and a[j] not in v) or (a[i] not in v and a[j] in v):
            cnt+=1
        i+=1
        j-=1
    return cnt

a=input()
s=a.split()
c=0
for i in s:
    p=fun(i)
    c+=p
print(c)