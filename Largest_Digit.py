n=int(input())#253
sum=0
m=0
while n:
    r=n%10#3,5
    if r>m:
        m=r#m=3,5
    n=n//10#25,2
print(m)
