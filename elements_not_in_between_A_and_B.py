n=int(input())
a=list(map(int,input().split()))
A,B=map(int,input().split())

for i in a:
    if i<A or i>B:
        print(i,end=" ")
if i>A and i<B:
    print("-1")
        
   