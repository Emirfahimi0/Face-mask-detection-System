import mysql.connector as mysql
from mysql import connector

mydb = mysql.connect(host="localhost",
                            user="root",
                            passwd="athris123",
                            database="new_db",
                        )

my_cursor = mydb.cursor()





#my_cursor.execute("INSERT INTO PERSONS (PERSONID,LASTNAME,FIRSTNAME,CITY) VALUES (%S,%s,%s,%s)", (1,"FAHIMI","EMIR","SUBANG JAYA"))
#mydb.commit()
#my_cursor.execute("CREATE TABLE UPLOAD (Upload_id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)")
my_cursor.execute("DESCRIBE UPLOAD")

for x in my_cursor:
    print(x)