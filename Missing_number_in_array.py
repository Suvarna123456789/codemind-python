n=int(input())
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    for i in range(1,a+1):
        if i not in l:
            print(i)