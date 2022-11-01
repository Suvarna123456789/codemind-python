n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,n-1):
    if a[i]%2==1 and a[i-1]%2==1 and a[i+1]%2==1:
        c=c+1
print(c)