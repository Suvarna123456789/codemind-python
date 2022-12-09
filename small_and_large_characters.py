a=input()
s=a.split()
for i in range(len(s)):
    print(min(s[i]),max(s[i]),end=" ")