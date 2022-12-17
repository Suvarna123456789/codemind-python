def fun(s):
    a=[]
    b=[]
    for i in range(len(s)):
        if s[i].isalpha():
            a.append(s[i])
        else:
            b.append(i)
    a.sort()
    for i in b:
        a.insert(i,s[i])
    s="".join(a)
    return s
a=list(map(str,input().split()))
for i in a:
    res=fun(i)
    print(res,end=" ")