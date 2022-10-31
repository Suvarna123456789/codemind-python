def rev(n):
    sum=0
    while n:
        r=n%10
        sum=sum*10+r
        n=n//10
    return sum
n,x=map(int,input().split())
r=n%10**x
p=rev(n)
s=0
for i in range(1,x+1):
    r1=p%10
    s=s*10+r1
    p//=10
print(abs(r-s))