a=[]
b=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
for i in a:
   
    if i not in b:
        b.append(i)
for i in b:
    count=0
    for j in a:
        if i==j:
            count=count+1
    print(i,"=",count)
