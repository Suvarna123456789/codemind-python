def gcd(a,b):
    t=2
    r=1
    while a>=t or b>=t:
        if a%t==0 and b%t==0:
            a=a//t
            b=b//t
            r=r*t
        else:
            t=t+1
    print(r)





a,b=map(int,input().split())
gcd(a,b)
