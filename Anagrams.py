a=input()
b=input()
a=a.lower()
b=b.lower()
c=0
for i in a:
    if i in b:
        c+=1
if c==len(a):
    print(True)
else:
    print(False)