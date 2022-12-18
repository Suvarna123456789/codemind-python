a=input()
b=input()
a=a.lower()
b=b.lower()
s1=a.split()
s2=b.split()
c=0
for i in s2:
    if s1.count(i)==1:
        if i in s1 and s2.count(i)==1:
            c+=1
print(c)