class name():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis(self):
        print("Name : ",self.name,"\nage:",self.age)
ob=name("Athul",23)
print(ob.dis())
n=input("Enter the name")   
a=int(input("age"))
ob=name(n,a)
print(ob.dis())