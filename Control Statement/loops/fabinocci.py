num=int(input("Enter the number : "))
f1=0
f2=1
f3=0

print(f1)
print(f2)
for i in range(1,num):
    f3=f1+f2
    f2=f1
    f1=f3
    print(f3)
