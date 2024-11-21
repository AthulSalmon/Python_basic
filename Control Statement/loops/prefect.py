n=int(input("Enter the number :"))
i=1
sum=0
temp=n
while i<n:
    if n%i==0:
        sum=sum+i
        print(sum)
    i=i+1
if temp==sum:
    print("prefact number")
else:
    print("Not",sum)
