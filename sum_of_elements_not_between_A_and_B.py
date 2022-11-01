n=int(input())
a=list(map(int,input().split()))
A,B=map(int,input().split())
b=[]
for i in a:
    if i>=A and i<=B:
        pass
    else:
        b.append(i)
print(sum(b))
    
