import sys
class Employee:
    def __init__(self,eno,en,s):
        self.__empno=eno
        self.__ename=en
        self.__sal=s
        print("Object Created...")
    def __del__(self):
        print("Object Deleted...")

emp1=Employee(101,"naresh",4000)
emp2=Employee(102,"suresh",6000)
emp3=emp1
emp4=emp1
emp5=emp1
print(sys.getrefcount(emp1))
emp3=None
emp4=None
print(sys.getrefcount(emp1))
emp5=None
emp1=None
emp2=None
