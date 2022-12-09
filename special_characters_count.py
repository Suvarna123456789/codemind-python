a=input()
c=0
for i in a:
    if i.islower() or i.isupper() or i==" ":
        pass
    else:
       #@ print(i)
        c+=1
print(c)