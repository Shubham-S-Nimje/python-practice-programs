def fun1():
    x=100 # Local Variable of fun1
    def fun2():
        y=200 # Local Variable of fun2
        x=300 # Local Variable of fun2
        print(x)
        print(y)
    fun2()
    print(x)

fun1()

