a=[]
lim=int(input("Enter the limit"))
for i in range(1,lim+1):
    ele=int(input())
    a.append(ele)
l=0
sl=0
for i in a:
    if i > l:
        sl = l
        l = i
    elif i > sl and i != l:
        sl = i
                  
print("The second largest element is : ",sl)

# a=[25,2,3,4,5,1,22]
# n=7
# big=a[0]
# for i in range(1,n):
#     if a[i]>big:
#         big=a[i]
# print("Largest number..",big)
# i=0
# while(1):
#     if a[i]!=big:
#         sbig=a[i]
#         break
#     i+=1
# for i in range(i+1,n):
#     if a[i]<big and a[i]>sbig:
#         sbig=a[i]
# print(sbig)