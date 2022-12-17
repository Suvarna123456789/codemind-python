n=input()
a=[]
c=[]
n=n.lower()
for i in n:
    if i not in a and i.isalpha():
        a.append(i)
print(len(a))