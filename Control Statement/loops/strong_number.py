num=int(input("Enter the number"))
i=0
temp=num
s=0
while num!=0:
    d=num%10
    fact=1
    while d>1:
        fact=fact*d
        d=d-1
    s=s+fact
    num=num//10
if s==temp:
    print("strong number",s)
else:
    print("Not a strong number",s)
