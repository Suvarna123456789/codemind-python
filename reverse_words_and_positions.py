def rev(n):
    s=''
    for i in range(-1,-len(n)-1,-1):
        s+=n[i]
    return s
n=input()
a=[]
s=n.split()
for i in s:
    a.append(rev(i))
#print(a)
for j in range(len(a)-1,-1,-1):
    print(a[j],end=" ")