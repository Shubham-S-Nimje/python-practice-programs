# Establishing connection to oracle database

import cx_Oracle

cn=cx_Oracle.connect("system/2512@localhost:1521/XE")
print("connection established")
cn.close()
