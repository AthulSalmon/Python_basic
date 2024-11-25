t=(1,2,3,3,2,1)
l = len(t) // 2
if t[:l] == t[-1:-l-1:-1]:
    print("symmetric")
else:
    print("not")
    
