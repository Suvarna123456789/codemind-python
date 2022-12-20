n=int(input())
row=[0 for i in range(n)]
d1=[row.copy() for i in range(n)]
d2=[row.copy() for i in range(n)]
empty=[row.copy() for i in range(n)]
for i in range(n):
    val=list(map(int,input().split()))
    for j in range(n):
        d1[i][j]=val[j]
for i in range(n):
    val=list(map(int,input().split()))
    for j in range(n):
        d2[i][j]=val[j]
for i in range(n):
    for j in range(n):
        empty[i][j]=abs(d1[i][j]-d2[i][j])
for i in empty:
    print(*i)

        