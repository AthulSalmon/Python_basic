a=[]
b=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
for i in a:
    if i not in b:
        b.append(i)    
print(b)
