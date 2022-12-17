n=input()
a=[]
c=0
s=n.lower()
#print(s)
for i in s:
    if s.count(i)==1:
        c+=1
        a.append(i)
if c!=0:
    for i in range(len(a)):
        print(a[0])
        break
else:
    print(-1)