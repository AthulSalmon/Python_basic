l=[1,2,3,1,2,3,4,5,6,7]
d={}
for i in l:
    count=0
    for j in l:
        if i==j:
            count=count+1
        d[i]=count
for x,y in d.items():
    print(y," time : ",x)

