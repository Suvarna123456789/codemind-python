n=int(input())
a=0
b=1
while a<=n:
    sum=a+b
    a=b
    b=sum
    
    if a==n:
        break
if a==n:
  print("True")
else:
  print("False")
    
