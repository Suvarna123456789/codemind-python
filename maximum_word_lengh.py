a=input()
l=[]
b=a.split()
for i in b:
    l.append(len(i))
print(max(l))