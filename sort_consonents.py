def fun(s):
    a1=[]
    a2=[]
    v="AEIOUaeiou"
    for i in range(len(s)):
        if s[i] not in v and s[i].isalpha():
            a1.append(s[i])
        else:
            a2.append(i)
    a1.sort()    
    for i in a2:
        a1.insert(i,s[i])
    s="".join(a1)    
    return s
s=list(map(str,input().split()))
for i in s:
    res=fun(i)
    print(res,end=' ')