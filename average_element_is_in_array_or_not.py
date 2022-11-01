n=int(input())
a=list(map(int,input().split()))
s=sum(a)
b=s//n
c=0
for i in a:
    if i==b:
        c=c+1
        break
if c!=0:
    print("True")
else:
    print("False")
