n=int(input())
for i in range(n+1,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()