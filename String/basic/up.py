ch=input("Enter the string")
l=len(ch)
for i in range(0,l,2):
    ch[i]=ch[i].upper()
print(ch)