a=[]
s=0
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
s=a[0]
for i in a:
    if s>i:
        s=i    
print(s)
