n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(0,len(a)):
    if i%2==0:
        c.append(a[i])
for i in c:
    if i%2==1:
        print("False")
        break
else:
    print("True")