def fun(n,a):
    pro=1
    for i in a:
        if i==n:
            pass
        else:
            pro=pro*i
    return pro
n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    r=fun(i,a)
    b.append(r)
print(*b)