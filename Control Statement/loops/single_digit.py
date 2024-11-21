num=int(input("Enter the number : "))
sum=0
while num!=0:
    r=num%10
    sum=r+sum
    num=num//10
    if sum>9 and num==0:
        num=sum
        sum=0
print(sum)
