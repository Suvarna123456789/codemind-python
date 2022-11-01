n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    if i%2==1:
        b.append(i)
for i in range(1,len(b)):
    B=len(b)
print(b[len(b)-1])