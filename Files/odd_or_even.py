n=int(input("enter the number of elements : "))
for i in range(0,n):
    num=int(input("Enter the number : "))
    f=open("Odd.txt","a")
    f1=open("Even.txt","a")
    if num%2==0:
        f1.write(str(num))
        f1.write("\n")
    else:
        f.write(str(num))
        f.write("\n")
    f.close()
    f1.close()