n=input()
s=[]
n=n.lower()
for i in n:
    if n.count(i)==1 and i.isalpha():
        s.append(i)
s.sort()
a=""
for i in s:
    a+=i
print(a)
    