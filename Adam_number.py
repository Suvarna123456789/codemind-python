def rev(n):
    sum=0
    while n:
        r=n%10
        sum=sum*10+r
        n=n//10
    return sum
def square(n):
    s=1
    s=n*n
    return s
def checkadam(n):
    b=square(rev(n))
    a=square(n)
    if a==rev(b):
        return True
    else:
        return False
    



n=int(input())
if checkadam(n):
    print("True")
else:
    print("False")
