a=input()
b=input()
a=a.lower()
b=b.lower()
c=0
#print(a,b)
s=a.split()
s1=b.split()
for i in s:
    if i in s1:
        c+=1
print(c)