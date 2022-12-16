r=int(input())
c=int(input())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
#print(*d)
s=0
for i in range(r):
    for j in range(c):
        s+=d[i][j]
print(s)