n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
b=[]
for i in a:
    if i<=avg:
        b.append(i)
print(len(b))