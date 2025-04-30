def fun1():
    x=100 # Local Variable of outer function
    def fun2():
        print(x) # "x" non local variable for fun2

    fun2()


fun1()
