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
rows=c.fetchmany(1)
print(rows)
rows=c.fetchmany(2)
print(rows)
rows=c.fetchmany(3)
print(rows)
cn.close()