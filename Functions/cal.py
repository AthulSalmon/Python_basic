def sum1(a,b):
    return a+b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b
def modu(a,b):
    return a%b
def sub(a,b):
    return a-b
while(1):
    print("1.Add \n2. sub \n3. mul \n4.div \n5. modulo \n6. exit")
    ch=int(input("Enter the choice"))
    if ch==1:
        n1=int(input("Enter te number"))
        n2=int(input("Enter te number"))
        print(sum1(n1,n2))
    elif ch==2:
        n1=int(input("Enter te number"))
        n2=int(input("Enter te number"))
        print(sub(n1,n2))
    elif ch==3:
        n1=int(input("Enter te number"))
        n2=int(input("Enter te number"))
        print(mul(n1,n2))
    elif ch==4:
        n1=int(input("Enter te number"))
        n2=int(input("Enter te number"))
        if n2!=0:
            print(div(n1,n2))
        else:
            print("Cannot div")
    elif ch==5:
        n1=int(input("Enter te number"))
        n2=int(input("Enter te number"))
        print(modu(n1,n2))
    else:
        break
    
