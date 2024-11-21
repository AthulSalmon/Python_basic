s=input("Eenter the string : ")
rev=""
temp=s
for i in s:
    rev=i+rev
if temp==rev:
    print("Palindrome")
else:
    print("not")
