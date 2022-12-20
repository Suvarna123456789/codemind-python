r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
o=0
e=0
for i in range(r):
    for j in range(c):
        if d[i][j]%2==0:
            e+=d[i][j]
        else:
            o+=d[i][j]
print(e,o)
