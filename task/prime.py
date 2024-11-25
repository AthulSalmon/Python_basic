num={1,2,3,4,5}
c=0
for j in num:
    if j < 2:
        continue 
    for i in range(2, int(j**0.5) + 1):
        if j % i == 0:
            break
    else:
        c+= 1
print(c)
