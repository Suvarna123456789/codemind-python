a=list(map(str,input().split()))
b=list(map(str,input().split()))
l1=[]
l2=[]
for i in a:
    l1.append(i.lower())
for i in b:
    l2.append(i.lower())
for i in l2:
    if i in l1:
        print(i,end=" ")