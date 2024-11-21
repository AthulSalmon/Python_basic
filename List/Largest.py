a=[]
s=0
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
l=a[0]
for i in a:
    if l<i:
        l=i
    
print(l)
