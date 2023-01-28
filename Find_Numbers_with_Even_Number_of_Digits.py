def fun(n):
    s=str(n)
    c=len(s)
    return c
n=int(input())
a=list(map(int,input().split()))
l=[]
c=0
for i in a:
    res=fun(i)
    l.append(res)
for i in l:
    if i%2==0:
        c+=1
print(c)
    
