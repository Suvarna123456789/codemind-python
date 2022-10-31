n=int(input())
pfs_n=0
for i in range(1,n):
    if n%i==0:
        pfs_n=pfs_n+i
if pfs_n>n:
    print("True")
else:
    print("False")