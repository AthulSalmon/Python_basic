num=int(input("Enter the number"))
i=0
sum=0
p=1
while num!=0:
    d=num%10
    sum=sum+d
    p=p*d
    num=num//10
if p==sum:
    print("Spy number")
else:
    print("Not aspy number")
