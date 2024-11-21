num=int(input("Enter the number : "))
sum=0
while num!=0:
    r=num%10
    sum=r+sum
    num=num//10
print(sum)
