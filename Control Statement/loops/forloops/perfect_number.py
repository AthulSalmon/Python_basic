n=int(input("Enter the number"))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if n==s:
    print("Prefect number")
else:
    print("No")
