a=[]
lim=int(input("Enter the limit for 1 array : "))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
b=[]
lim=int(input("Enter the limit for second array: "))
for i in range(1,lim+1):
    ele=int(input())
    b.append(ele)

c=a+b
l=len(c)
for i in range(0,l):
    for j in range(0,i):
        if c[i]<c[j]:
            temp=c[i]
            c[i]=c[j]
            c[j]=temp
print("Frist array : ",a)
print("Secomnd array : ",b)
print("sorted array : ",c)

