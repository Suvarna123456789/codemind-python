n=int(input())
for i in range(n):
    s=input()
    t=s
    c=[]
    for i in range(-1,-len(s)-1,-1):
        c.append(s[i])
    c=''.join(c)
    if c!=t:
        print("NO")
    elif c==t and len(c)%2!=0:
        print("YES ODD")
    elif c==t and len(c)%2==0:
        print("YES EVEN")
