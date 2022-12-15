a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_p=0
b_p=0
for i in range(len(a)):
    if a[i]>b[i]:
        a_p+=1
    elif a[i]==b[i]:
        continue
    else:
        b_p+=1
print(a_p,b_p)