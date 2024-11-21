num=[1,4,5,7,9]
l=len(num)

temp=num[0]
i=0
while i<l:
    if num[i]>temp:
        temp=num[i]
    i=i+1
print(temp)
    
