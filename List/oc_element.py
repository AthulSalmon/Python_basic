a=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
ele=int(input("The number: "))
for i in range(0,lim):
    if a[i]==ele:
        print(i+1)
        break
else:
    print("not found")

