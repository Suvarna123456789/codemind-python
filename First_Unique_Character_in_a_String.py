a=input()
for i in range(len(a)):
    if a.count(a[i])==1:
        print(i)
        break
else:
    print(-1)
    