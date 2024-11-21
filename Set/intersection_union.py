a={'a','b','c','d'}
b={1,2,3,4}
c=a.union(b)
print(c)

a={'a','b','c','d'}
b={1,2,3,4}
a.update(b)
print(a)

a={'a','b','c','d',1}
b={1,2,3,4,'a'}
c=a.intersection(b)
print(c)

a={'a','b','c','d',1}
b={1,2,3,4,'a'}
a.intersection_update(b)
print(a)