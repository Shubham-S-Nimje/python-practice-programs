def fun1():
    print("Hello")
    return
    print("Bye")

def fun2():
    return 10
    return 20
    return 30

def fun3():
    return 10,20,30,40,50


fun1()
x=fun2()
print(x)
y=fun3()
print(y)