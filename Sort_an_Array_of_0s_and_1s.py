a=int(input())
c=[]
d=[]
l=list(map(int,input().split()))
for i in l:
    if i==0:
        c.append(i)
    else:
        d.append(i)
c.extend(d)
print(*c)