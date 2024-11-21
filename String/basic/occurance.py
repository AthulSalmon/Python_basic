s="Hi Python "
a=input("Enter the string to search : ")
count=0
for i in s:
    if a in s:
        count=count+1
if count==0:
    print("No")
else:
    print("Yes")
