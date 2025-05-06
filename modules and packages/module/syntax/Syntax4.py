# Module1.py
x=100 # Global Variable
def fun1():
    print("inside fun1 of module1")

def fun2():
    print("inside fun2 of module1")

def fun3():
    print("inside fun3 of module1")
    

# Module5.py
from module1 import fun1 as f1

def fun1():
    print("inside fun1 of module5")



fun1()
f1()

# Output
# inside fun1 of module5
# inside fun1 of module1

