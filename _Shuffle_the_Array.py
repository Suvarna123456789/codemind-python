n=int(input())
a=list(map(int,input().split()))
dup=[]
for i in range(n//2,n):
    dup.append(a[i])
d=int(input())
b=[]
c=[]
for i in range(0,n//2):
    b.append(a[i])
for i in range(len(b)):
    print(b[i],dup[i],end=" ")