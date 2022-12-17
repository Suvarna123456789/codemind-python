n=input()
a=[]
n=n.lower()
for i in n:
    if i not in a and i.isalpha():
        a.append(i)
a.sort()
n="".join(a)
print(n)