s=int(input())
sl=list(map(int,input().split()))
e=int(input())
el=list(map(int,input().split()))
q=int(input())
c=0
for i in range(e):
    if q>=sl[i] and q<=el[i]:
        c+=1
print(c)
