n=int(input())
a=list(map(int,input().split()))
a.insert(n,a[0])
a.insert(n+1,a[1])
n=n+2
i,j=0,2
c=0
while i<n and j<n:
    if a[i]%2==0 and a[j]%2==1 or a[i]%2==1 and a[j]%2==0:
        c=c+1
    i=i+1
    j=j+1
print(c)