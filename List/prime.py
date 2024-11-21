a=[]
b=[]
c=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
for i in a:
    count=0
    for j in range(2,i):
        if i%j==0:
            count=count+1
    if count==0:
        b.append(i)
    else:
        c.append(i)
print(a)
print("prime=",b)
print("Not prime=",c)
