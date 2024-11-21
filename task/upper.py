ch=input("Enter the string : ")
l=len(ch)
up=0
lw=0
for i in range(l):
    if ch[i]==ch[i].upper() and ch[i]!=" ":
        up+=1
    elif ch[i]==ch[i].lower() and ch[i]!=" ":
        lw+=1
print("Upper :",up)
print("lower: ",lw)
    