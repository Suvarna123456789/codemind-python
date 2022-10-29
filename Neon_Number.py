def neonnumber(n):
    m=n#m=9
    n=n*n#n=81
    sum=0
    while n:
        d=n%10#d=1,0
        sum=sum+d#sum-1,2
        n=n//10#n=8,0
    if m==sum:
        print("Neon Number")
    else:
        print("Not Neon Number")
n=int(input())
neonnumber(n)
