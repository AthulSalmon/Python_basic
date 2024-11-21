ch=input("Enter the string")
l=len(ch)
for i in range(l):
    if i%2==0:
        print(ch[i],end="")
    else:
        print(ch[i].upper(),end="")
