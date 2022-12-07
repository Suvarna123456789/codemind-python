a=input()
s="aeiou"
c=0
for i in s:
    if i in a:
        c+=1
if c==len(s):
    print("True")
else:
    print("False")