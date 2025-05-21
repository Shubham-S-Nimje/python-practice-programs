# Write a program to insert data into emp_tab
import cx_Oracle

cn=cx_Oracle.connect("system/2512@localhost:1521/XE")
c=cn.cursor()
while True:
    eno=int(input("EmployeeNo :"))
    en=input("EmployeeName :")
    j=input("EmployeeJob :")
    s=float(input("EmployeeSal :"))
    cmd='''insert into emp_tab values(:1,:2,:3,:4)'''
    c.execute(cmd,(eno,en,j,s))
    print("Employee Created...")
    ans=input("Add another employee?")
    if ans=="no":
        break

cn.commit()
cn.close()
