class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def det(self,name,age):
        print(f" Name : {self.name}\nAge : {self.age}")
class student(person):
        def __init__(self, name, age,m):
            super().__init__(name, age)
        def cal(self):
            return sum(self.m)/len(self.m)

while(1):
    print(f"1.Enter the details\n2.display\n3.avg\n4.exit")
    c=int(input("Enter the choice : "))
    if c==1:
       name=input("Enter the name : ")
       age=int(input("Enter the age : "))
       m=list(map())
       ob.student(name,age,m)
    elif c==2:
        
        
    elif c==3:
        
    else:
        break
