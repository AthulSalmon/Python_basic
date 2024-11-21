num=int(input("enter the number :"))
for i in range(2,num+1):
    if(num%i==0):
        break
if i==num:
    print("prime")
else:
    print("Not a prime")
