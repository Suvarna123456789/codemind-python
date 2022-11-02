n=int(input())
a=list(map(int,input().split()))
b=[]
avg=sum(a)//n
for i in a:
    if i>=avg:
        b.append(i)
print(len(b))