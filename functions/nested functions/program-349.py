def fun1():
    print("outer function")
    def fun2():
        print("inner function")
    fun2()



fun1()
