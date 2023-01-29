t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    c=[]
    for i in l1:
        c.append(i)
    for i in l2:
        c.append(i)
    c.sort()
    print(*c)