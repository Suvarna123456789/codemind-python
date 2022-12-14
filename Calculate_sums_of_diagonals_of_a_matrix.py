n=int(input())
row=[0 for i in range(n)]
d=[row.copy() for i in range(n)]
for i in range(n):
    val=list(map(int,input().split()))
    for j in range(n):
        d[i][j]=val[j]
sum=0
for i in range(n):
    for j in range(n):
        if i==j:
            sum+=d[i][j]
k=1
for i in range(n):
    sum+=d[i][n-k]
    k+=1
for i in range(n):
    for j in range(n):
        if i==j:
            if str(i)+str(j)==str(i)+str(n-j-1):
                sum-=d[i][j]
print(sum)
