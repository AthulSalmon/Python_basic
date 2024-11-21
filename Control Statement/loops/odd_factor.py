num=int(input("Enter the number"))
i=1
sum=0
while i<=num:
    if num%i==0:
        if i%2!=0:
            sum=sum+i
    i=i+1
print(sum)
