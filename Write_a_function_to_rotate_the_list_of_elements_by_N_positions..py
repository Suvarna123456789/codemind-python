def fun(l):
    arr=[]
    arr=append(l[-1])
    for i in range(0,len(l)-1):
        arr.append(l[i])
    return arr
n=int(input())
l=list(map(int,input().split()))
r=int(input())
for i in range(r):
    res=fun(i)
print(res)