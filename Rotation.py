def fun(l):
    a=[]
    a.append(l[-1])
    for i in range(len(l)-1):
        a.append(l[i])
    return a
    
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    for i in range(b):
        res=fun(l)
        l=res
    print(*l)
        
        
