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
c.execute("select * from stud_marks")
row1=c.fetchone()
print(row1)
row2=c.fetchone()
print(row2)
row3=c.fetchone()
print(row3)
row4=c.fetchone()
print(row4)
row5=c.fetchone()
print(row5)
row6=c.fetchone()
print(row6)
cn.close()
