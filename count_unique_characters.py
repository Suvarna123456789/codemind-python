n=input()
s=n.lower()
c=0
for i in range(len(s)):
    if n.count(s[i])==1 and s[i].isalpha():
        c+=1
print(c)