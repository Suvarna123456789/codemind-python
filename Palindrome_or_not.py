n=input()
c=""
n=n.lower()
t=n
for i in range(-1,-len(n)-1,-1):
    c+=n[i]
if c==t:
    print(True)
else:
    print(False)