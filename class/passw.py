class user():
    def __init__(self,us):
        self.us=us
        self.ps=""
    def set_password(self,ps):
        if self.ps=="":
            self.ps=ps
        else :
            print("You Are already set a password : ")
    def reset_password(self,rs,ps):
        self.ps1=ps
        self.rs=rs
        if self.ps!="": 
            if self.ps==self.ps1:
                self.ps=self.rs
                print("Password updated : ")
        else:
            print(" You are not set a password : ")

us=input("Enter the number :")
ob=user(us)
while True:
    print(f"\n1.set password\n2.reset password\n3.display\n4.exit")
    c=int(input("Enter the chpoice : "))
    if c==1:
        ps=input("Enter the password :")
        ob.set_password(ps)
    elif c==2:
        ps=input("Enter the old password :")
        rs=input("Enter the  new password :")
        ob.set_password(rs,ps)
    elif c==3:
        print(f"User name : {ob.us}")
        l=len(ob.ps)
        for i in range(l):
            print("*",end="")
    else:
        break


