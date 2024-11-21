# lim=int(input("enter the limit :"))
# for i in range(1,lim+1):
#     for j in range(2,i+1):
#         if(i%j==0):
#             break
#     if j==i:
#         print(i)


l=int(input())
u=int(input())
for i in range(l,u+1):
	if l==1:
		continue
	for j in range(2,i):
		if i%j==0:
			break
	else:
		print(i)
    