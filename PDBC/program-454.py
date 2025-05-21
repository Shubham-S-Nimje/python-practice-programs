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
rows=c.fetchall()
print(rows)
for row in rows:
    rno,name,sub1,sub2,sub3,total,avg=row
    res="PASS" if sub1>=40 and sub2>=40 and sub3>=40 else "FAIL" # type: ignore
    print(rno,name,sub1,sub2,sub3,total,avg,res)

cn.close()