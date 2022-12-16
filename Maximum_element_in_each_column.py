def m(r,c,d):
    m_c=[0 for i in range(c)]
    for i in range(c):
        c=0
        for j in range(r):
            if d[j][i]>c:
                c=d[j][i]
        print(c)


r,c=map(int,input().split())
row=[0 for i in range(c)]
d=[row.copy() for i in range(r)]
for i in range(r):
    val=list(map(int,input().split()))
    for j in range(c):
        d[i][j]=val[j]
r=m(r,c,d)