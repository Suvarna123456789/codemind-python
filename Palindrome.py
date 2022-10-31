n=int(input())
N=n
sum=0
while n:
    r=n%10
    sum=sum*10+r
    n//=10
if N==sum:
    print("True")
else:
    print("False")