a=input()
s='aeiou'
c=0
for i in s:
    if i in a:
        pass
    else:
        print(i,end=' ')
        c+=1
if c==0:
    print(0)