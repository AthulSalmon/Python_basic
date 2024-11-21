num=int(input("Enter the number : "))
temp=num
rev=0
while num!=0:
    d=num%10
  
    rev=rev*10+d
    num=num//10
if temp==rev:
    print("palindrome")
else:
    print("Not a palindrome")

print(rev)
