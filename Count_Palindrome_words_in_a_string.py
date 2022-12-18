def fun(a):
    a=a.lower()
    c=''
    for i in range(-1,-len(a)-1,-1):
        c+=a[i]
    return c
        
n=input()
n=n.lower()
s=n.split()
c=0
for i in s:
    t=i
   # print(i,end=" ")
    res=fun(i)
    #print(res,end=" ")
    if res==t:
        
        c+=1
print(c)