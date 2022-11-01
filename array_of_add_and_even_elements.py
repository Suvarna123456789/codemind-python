n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if i%2==1:
        b.append(i)
    if i%2==0:
        c.append(i)
b.extend(c)
print(*b)
