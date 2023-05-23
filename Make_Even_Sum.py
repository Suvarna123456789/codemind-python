n=int(input())
lst=list(map(int,input().split()))
if sum(lst)%2:
    print(0)
else:
    print(1)