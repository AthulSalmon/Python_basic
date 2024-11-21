cb={}
while(1):
    print("1.ADD a contact\n2.Edit a contact\n3.Delete a contact\n4.Search a contact\n5.Display a contact\n6.Exit")
    ch=int(input("Enter the choice :"))
    if ch==1:
        name=input("Enter the name to add : ")
        no=int(input("Enter the number"))
        cb[name]=no
        print("Added Successfully")
    elif ch==2:
        name=input("Enter the name to edit : ")
        no=int(input("Enter the number"))
        cb[name]=no
        print("Edit Successfully")
    elif ch==3:
        name=input("Enter the name to delete : ")
        cb.pop(name)
                
        print("delete Successfully")
    elif ch==4:
        name=input("Enter the name to search : ")
        print("Phone number",name," : ",cb[name])
    elif ch==5:
        print("Name\t\tPhone no")
        for x,y in cb.items():
            print(x,"\t\t",y)
    elif ch==6:
        break
    else:
        print("Wrong choice")
            
        

        
