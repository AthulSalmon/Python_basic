num=int(input("Enter the number"))
temp=0
while num!=0:
    d=num%10
    if temp<=d:
        temp=d
    num=num//10
print(temp)
