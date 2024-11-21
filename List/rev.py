a=[]
rev=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
for i in a:
    rev.insert(1,i)
print(rev)
