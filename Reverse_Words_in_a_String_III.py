def fun(s):
    c=[]
    for i in range(-1,-len(s)-1,-1):
        c.append(s[i])
    c=''.join(c)
    return c

n=input()
s=n.split()
d=[]
for i in s:
    c=fun(i)
    d.append(c)
d=" ".join(d)
print(d)