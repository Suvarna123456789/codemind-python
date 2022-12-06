a=input()
s='aeiouAEIOU'
c=0
d=[]
for i in a:
    if i in s and i not in d:
        d.append(i)
print(*d)
        
