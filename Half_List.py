n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(-1,-n//2-1,-1):
    a.append(l[i])
for i in range(0,n//2):
    a.append(l[i])
print(*a)