def digits(n):
    c=0
    while n:
        r=n%10
        n=n//10
        c=c+1
    return c
n=int(input())
temp=n
r=0
s=0
d=digits(n)
while n:
    r=n%10
    s=s+int(r**d)
    n=n//10
    d=d-1
if s==temp:
    print("True")
else:
    print("False")




