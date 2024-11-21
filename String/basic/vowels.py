s=input("Enter the string : ")
temp=s.upper()
count=0
for i in temp:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        count=count+1
print("The number of vowels : ",count)
