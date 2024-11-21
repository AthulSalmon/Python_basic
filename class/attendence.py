class emp:
    def __init__(self,name,id,sal,dept):
      self.name=name
      self.id=id
      self.sal=sal
      self.da=self.sal*0.1
      self.hra=self.sal*0.2
      self.pf=self.sal*0.15
      self.sal=(self.da+self.hra+self.sal)-self.pf
      self.dept=dept
      
class student(emp):
    def __init__(self, name, id, sal, dept):
        super().__init__(name, id, sal, dept)
        self.s=[]
    def cal(self,n):
        self.n=n
        print("0 of A and  1 for P")
        for i in range(self.n):
            e=int(input())
            self.s.append(e)
    def dis_attendence(self):
        print("name: ",self.name,"\nId : ",self.id,"\nsalary : ",self.sal,"\nda : ",self.da,"\nhra : ",self.hra,"\npf : ",self.pf)
        for i in self.s:
            if self.s[i]==1:
                print(f" persent {i+1}")
        for i in self.s:
            if self.s[i]==1:
                print(f" absent {i+1}")
    
        
            
       
n=int(input("Enter the number of teacher : "))
i=0
t_l=[]
for i in range(0,n):
    name=input(" name :")
    id=int(input(" teacher id : "))
    sal=int(input(" teacher salary : "))
    dept=input(" dept : ")
    n1=int(input("Enter the no of students : "))
    o=student(name,id,sal,dept)
    o.cal(n1)
    t_l.append(o) 

   
for i in range(n):
    print(t_l[i].dis_attendence())



