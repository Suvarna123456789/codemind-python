def fun(i,l):
    c=0
    for j in l:
        if i>j:
            c+=1
    return c
n=int(input())
l=list(map(int,input().split()))
c=0
a=[]
for i in l:
    res=fun(i,l)
    a.append(res)
print(*a)
