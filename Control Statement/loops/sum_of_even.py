n=int(input("Enter the limit"))
i=0
sum=0
while i<n:
    num=int(input("Enter the number"))
    if num%2==0:
        sum=sum+num
    i=i+1
print("sum =",sum)
