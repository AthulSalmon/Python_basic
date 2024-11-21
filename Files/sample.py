#create and write
# f=open("sample.txt","w")
# f.write("Hi all")
# f.close()

#create
# f=open("sample2.txt","x")
# f.close()

#append
# f=open("sample.txt","a")
# f.write("\nHi python")
# f.close()

#open with
with open("sample.txt","r") as file:
    result=file.read()
    print(result)
file.close()

    