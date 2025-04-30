def fun1():
    def fun2():
        print("inner function")

    return fun2

a=fun1()
a()
