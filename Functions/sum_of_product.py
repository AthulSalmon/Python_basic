def sum(*n):
    p=1
    for i in n:
        p=p*i
    print(p)
n=int(input("Enter the limit : "))
l1=[]
for i in range(n):
    e=int(input())
    l1.append(e)
l1=tuple(l1)
sum(*l1)