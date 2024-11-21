import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    db="aug_27"
    
)
def list1():
    curs = db.cursor()
    curs.execute("Select *from emp1")
    for i in curs:
        print(f'''\t----------------
              id={i[0]}
              name={i[1]}
              age={i[2]}
              salary={i[3]}''')
    curs.close()
def add(name,age,salary):
    curs = db.cursor()
    quary=("insert into emp1(emp_name,emp_age,salary)values(%s,%s,%s)")
    value=(name,age,salary)
    curs.execute(quary,value)
    db.commit()
def edit(name,salary):
    curs = db.cursor()
    q="Update emp1 set salary=%s where emp_name=%s"
    value=(salary,name)
    curs.execute(q,value)
    db.commit()
def delete1(age):
    curs = db.cursor()
    query = "DELETE FROM emp1 WHERE emp_age = %s"
    value = (age,)
    curs.execute(query, value)
    db.commit()
    print("Record deleted successfully!")

while(1):
    print("1.List\n2.Add\n3.Edit\n4.Delect\n5.Exit")
    ch=int(input("Enter the choice : "))
    if(ch==1):
        list1()
    elif(ch==2):
        name=input("Enter the name :")
        age=int(input("Enter the age"))
        salary=int(input("Enter the salary"))
        add(name,age,salary)
    elif(ch==3):
        name=input("Enter the name  :")
        salary=int(input("Enter the  new salary"))
        edit(name,salary)
    elif(ch==4):
        age=int(input("Enter the age  :"))
        delete1(age,)    
    elif(ch==5):
        break
    else:
        print("Wrong choice...!")
    

db.close()


