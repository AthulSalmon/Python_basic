class bank():
    def __init__(self,acc):
       self.acc=acc
       self.balance=0 
    def deposit(self,amt):
        self.amt=amt
        self.balance=self.amt+self.balance
        print(f"The balance is : {self.balance}")
    def withdraw(self,wd):
        self.wd=wd
        if self.balance>=wd:
            self.balance=self.balance-self.wd
            print(f"The balance is : {self.balance}")
        else:
            print("Invalid ammount")
    
acc=int(input("Enter the acc no"))
ob=bank(acc)
while(1):
    print("1.Deposit\n2.Widhdraw\n3.Balance\n4.Exit")
    ch=int(input("Enter the choice : "))
    if(ch==1):
        amt=int(input("The amount to deposit :"))
        ob.deposit(amt)
    elif(ch==2):
        wd=int(input("The amount to withdraw :"))
        ob.withdraw(wd)
    elif(ch==3):
        print(f" The balance is : {ob.balance}")
    elif(ch==4):
        break
    else:
        print("Wrong choice...!")
    