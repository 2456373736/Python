n=int(input("n:"))
i=1
sum=0
while i<=n:
    if i%2==0:
        sum=sum+i
    i=i+1
print("sum=",sum)
