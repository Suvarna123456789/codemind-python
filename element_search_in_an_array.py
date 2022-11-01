n=int(input())
a=list(map(int,input().split()))
e = int(input())
c=0
for i in a:
    if i == e:
        c+=1
        break
if c!=0:
    print("True")
else:       
    print("False")
