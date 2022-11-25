n=int(input())
a=list(map(int,input().split()))
c=0
b=[]
for i in a:
    if a.count(i)==1:
        if i in a and i not in b:
            b.append(i)
            c+=1
if c==0:
    print(-1)
else:
    print(max(b))