lim=int(input("enter the limit"))
a=[]
b=[]
c=[]
for i in range(0,lim):
    ele=int(input())
    a.append(ele)
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print("List=",a)
print("Even=",b)
print("odd=",c)
