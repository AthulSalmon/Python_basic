class emp:
    def __init__(self,name,id,sal):
      self.name=name
      self.id=id
      self.sal=sal
      self.da=self.sal*0.1
      self.hra=self.sal*0.2
      self.pf=self.sal*0.15
      self.sal=(self.da+self.hra+self.sal)-self.pf
    def dis(self):
       print("name: ",self.name,"\nId : ",self.id,"\nsalary : ",self.sal,"\nda : ",self.da,"\nhra : ",self.hra,"\npf : ",self.pf)
       
     
name=input(" name :")
id=int(input(" emp id : "))
sal=int(input(" emp id : "))
o=emp(name,id,sal)
name=input(" name :")
id=int(input(" emp id : "))
sal=int(input(" emp id : "))
o1=emp(name,id,sal)
print(o.dis())
print(o1.dis())



