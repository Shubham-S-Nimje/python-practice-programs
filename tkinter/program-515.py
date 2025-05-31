class Employee:
    def __init__(self,eno,en,s):
        self.__empno=eno
        self.__ename=en
        self.__sal=s
        print("Object Created...")
    def __del__(self):
        print("Object Deleted...")


def fun1():
    emp1=Employee(1,"suresh",5000)



fun1()
