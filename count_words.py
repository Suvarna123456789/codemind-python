def fun(n):
    c=0
    v="aeiouAEIOU"
    if n[0] in v and n[len(n)-1] not in v:
        c+=1
    return c
a=input()
s=a.split()
res=0
for i in s:
    c=fun(i)
    res+=c
print(res)