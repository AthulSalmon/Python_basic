l=int(input("Enter the lower limit "))
u=int(input("Enter the upper limit "))
for i in range(l,u):
    temp=i
    l=len(str(i))
    sum=0
    while i!=0:
        d=i%10
        d=d**l
        sum=sum+d
        i=i//10
    if sum==temp:
        print(sum)