import mysql.connector
c = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
    
)
curs = c.cursor()
curs.execute("SHOW DATABASES")
for db in curs:
    print(db)
curs.close()
c.close()