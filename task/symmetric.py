ch=input("Enter the string : ")
l=len(ch)
l2=l//2
rev=""
s=""
s2=""
for i in ch:
    rev=i+rev
for i in range(l2):
    s=s+ch[i]
for i in range(l2,l):
    s2=s2+ch[i]
if(rev==ch):
    print("palindrome")
else:
    print("Not a palindrome")
if(s==s2):
    print("Symmetric")
else:
    print("Not a symmetric")

