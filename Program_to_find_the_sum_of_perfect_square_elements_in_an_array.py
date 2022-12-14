import math
def fun(n):
    sqrt = math.sqrt(n)
    if(sqrt-int(sqrt))==0:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=[]
for i in l:
    #print(l)
    if fun(i)==True:
        c.append(i)
print(sum(c))
        
