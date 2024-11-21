class student:
    x="hi"
    def display(self,name):
        self.name1=name
        print(self.x,self.name1)
obj=student()
print(obj.x)
print(obj.display("Athul"))