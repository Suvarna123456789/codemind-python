a=input()
b=input()
a=a.lower()
b=b.lower()
n=""
for i in a:
    if i in b and i.isalpha():
        pass
    else:
        if i not in n and i.isalpha():
            n+=i
for i in b:
    if i in a:
        pass
    else:
        if i not in n and i.isalpha():
            n+=i
n=list(n)
n.sort()
n="".join(n)
print(n)