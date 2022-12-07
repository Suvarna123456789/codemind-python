def fact(n):
    fs=0
    for i in range(1,n+1):
        if n%i==0:
            fs+=i
    return fs
            


s=list(map(int,input().split(',')))
a=[]
for i in s:
    if fact(i) in s:
        a.append(i)
a.sort()
if len(a)==0:
    print("-1")
else:
    print(*a)
