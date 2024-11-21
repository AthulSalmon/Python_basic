with open("sample.txt","r") as file:
    result=file.read()
    result=result.upper()
    l=len(result)
    c=0
    for i in range(l):
        if result[i]=="A" or result[i]=="E" or result[i]=="I" or result[i]=="O" or result[i]=="U":
            c=c+1
print(c)
file.close()