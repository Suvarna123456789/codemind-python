n=int(input())
m=len(str(n))
t=0
c=0
while n:
    r=n%10
    if r%2==0:
        c=c+1
    elif r%2==1:
        t=t+1
    n=n//10
if m==c:
    print("Even")
elif m==t:
    print("Odd")
else:
    print("Mixed")