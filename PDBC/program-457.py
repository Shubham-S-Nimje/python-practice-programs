# Write a program to delete a student from stud_marks table

import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

cn=mysql.connector.connect(database= os.getenv('MYSQL_NAME'),
                   user= os.getenv('MYSQL_USER'),
                   password= os.getenv('MYSQL_PASSWORD'),
                   host= os.getenv('MYSQL_HOST'),
                   port= os.getenv('MYSQL_PORT'))

print("connection established...")

c=cn.cursor()
rno=int(input("Rollno Delete :"))
c.execute("delete from stud_marks where rollno=%s",params=(rno,))
x=c.rowcount
if x==0:
    print("Invalid Rollno")
else:
    print("Student Details are Deleted")
    cn.commit()

cn.close()
