a=[]
s=0
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
for i in a:
    s=s+i
print(s)
