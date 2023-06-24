import mysql.connector as mysql

db = mysql.connect(host = "localhost" , user = "root" ,passwd="")
myscu = db.cursor()
myscu.execute("CREATE DATABASE Bank") 
db.commit()
db.close()
print("succesffuly created databse ")