def rev(n):
    s=''
    for i in range(-1,-len(n)-1,-1):
        s+=n[i]
    return s
n=input()
s=n.split()
for i in range(0,len(s)):
    if i%2==0:
        print(rev(s[i]),end=" ")
    else:
        print(s[i],end=" ")