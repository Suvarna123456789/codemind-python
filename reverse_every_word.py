def rev(n):
    s=''
    for i in range(-1,-len(n)-1,-1):
        s+=n[i]
    return s
n=input()
s=n.split()
for i in s:
    print(rev(i),end=" ")