num=int(input("Enter the limit"))
sum=0
for i in range(0,num):
    ele=int(input("Enter the number"))
    if ele%2==0:
        sum=sum+ele
print(sum)