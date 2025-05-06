# Module1.py
x=100 # Global Variable
def fun1():
    print("inside fun1 of module1")

def fun2():
    print("inside fun2 of module1")

def fun3():
    print("inside fun3 of module1")

# Module2.py
import module1
import math

print(module1.x)
module1.fun1()
module1.fun2()
module1.fun3()
res1=math.sqrt(9)
res2=math.factorial(12)
print(res1)
print(res2)

# Output
# 100
# inside fun1 of module1
# inside fun2 of module1
# inside fun3 of module1
# 3.0
# 479001600

