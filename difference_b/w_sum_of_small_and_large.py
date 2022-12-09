def fun(a):
    min_s=0
    max_s=0
    min_s+=ord(min(a))
    return min_s
def funn(b):
    max_s=0
    max_s+=ord(max(b))
    return max_s
s=input()
l=[]
h=[]
a=s.split()
for i in a:
    c=fun(i)
    d=funn(i)
    l.append(c)
    h.append(d)
print(abs((sum(l))-sum(h)))