def fun(n):
    for i in n:
        return i
    
a=input()
s=a.split()
for i in s:
    c=fun(i)
print(c)