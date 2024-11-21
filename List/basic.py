a=[1,'all',9,8.0,9,'hi']
print(a)
a[0]='Athul'
print(a)
#append
a=[1,'all',9,8.0,9,'hi']
print(a)
a.append("Athul")
print(a)
#insert
a=[1,'all',9,8.0,9,'hi']
print(a)
a.insert(1,"Athul")
print(a)
# add to list
a=[1,2,4.5,8]
b=['hi','all']
print(a+b)
a.extend(b)
print(a)
a.clear()
print(a)
del b
print(b)