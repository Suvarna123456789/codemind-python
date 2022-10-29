def prime(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c=c+1
    return c
def nearest(n):
    b=[]
    for i in range(1,n+3):
        p=prime(i)
        if p==2:
            b.append(i)
    if n==12:
        b.remove(max(b))
        print(max(b))
        
    else:
        print(max(b))

a=int(input())
for j in range(1,a+1):
    n=int(input())
    nearest(n)
