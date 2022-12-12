def fun(n):
    c=0
    while n:
        r=n%10
        n=n//10
        c=c+1
    return c
a=int(input())
l=list(map(int,input().split()))
dic={}
d=[]
for i in l:
    c=fun(i)
    dic[i]=c
for k in dic.values():
    d.append(k)
print(d.count(min(d)))
