n=int(input())
a=list(map(int,input().split()))
a.reverse()
p=0
j=0
for i in range(0,n):
    p=p+a[i]*pow(2,j)
    j=j+1
    
  
print(p)