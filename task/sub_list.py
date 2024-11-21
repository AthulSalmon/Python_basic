li=[1,2,3,4,5,6,7,9,10]
l1=len(li)
b=[]
l=int(input("Enter the length"))
for i in range(l):
    e=int(input("Enter th values "))
    b.append(e)
for i in range(l1):
    if li[i:i+3]==b:
        print("present")
        break
else:
    print("not")

