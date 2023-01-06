r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
a=[0 for i in range(c)]
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
for i in range(c):
    for j in range(r):
        a[i]+=d[j][i]
print(*a)