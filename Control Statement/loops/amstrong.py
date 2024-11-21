num=input("Enter the number")
l=len(num)
num=int(num)
temp=num
sum=0
while num!=0:
    d=num%10
    d=d**l
    sum=sum+d
    num=num//10
if sum==temp:
    print("Amstrong",sum)
else:
    print("Not a amstrong",sum)
