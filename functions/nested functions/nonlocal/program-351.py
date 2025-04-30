def fun1():
    x=100 #local variable of fun1
    print(f'local variable of fun1 x={x}')
    def fun2():
        nonlocal x
        x=400
    fun2()
    print(f'local variable of fun1 x={x}')
    

fun1()
