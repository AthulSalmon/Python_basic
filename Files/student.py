n=int(input("enter the number of student : "))
for i in range(0,n):
    print("Enter the details of the student",i+1)
    name=input("Enter the name : ")
    age=input("Enter the age :")
    g=input("Enter the garde : ")
    f=open("student.txt","a")
    f.write("Name : ")
    f.write(name)
    f.write("\n")
    f.write("Age : ")
    f.write(age)
    f.write("\n")
    f.write("Grade : ")
    f.write(g)
    f.write("\n")
    f.close()