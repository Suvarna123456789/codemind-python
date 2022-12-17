a=input()
b=input()
a=a.lower()
b=b.lower()
c=0
cnt=[]
for i in a:
    if i not in b and i.isalpha():
        if i not in cnt:
            cnt.append(i)
for i in b:
    if i not in a and i.isalpha():
        if i not in cnt:
            cnt.append(i)
print(len(cnt))