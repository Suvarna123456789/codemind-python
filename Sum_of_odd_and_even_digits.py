n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(0,len(a)):
    if i%2==0:
        b.append(a[i])
    if i%2==1:
        c.append(a[i])
d=sum(b)
e=sum(c)
if d-e==0:
    print("YES")
else:
    print("NO")