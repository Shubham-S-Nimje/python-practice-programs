# Write a program to read employee details from emp_tab

import cx_Oracle

cn=cx_Oracle.connect("system/2512@localhost:1521/XE")
c=cn.cursor()
c.execute("select * from emp_tab")
rows=c.fetchall()
for row in rows:
    print(row)

cn.close()
