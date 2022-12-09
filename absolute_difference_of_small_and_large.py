def fun(n):
    return abs((ord(max(n)))-ord(min(n)))

a=input()
s=a.split()
l=[]
for i in s:
    c=fun(i)
    l.append(c)
print(*l)