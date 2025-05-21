# Write a program to create table in oracle database

import cx_Oracle

cn=cx_Oracle.connect("system/2512@localhost:1521/XE")
c=cn.cursor()
cmd='''create table emp_tab(empno number(5) primary key,
ename varchar2(20),
job varchar2(20),
sal number(10,2))'''
c.execute(cmd)
print("table created...")
cn.close()
