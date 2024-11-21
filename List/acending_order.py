a=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
temp=0
for i in range(0,lim):
    for j in range(0,i):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(a)
