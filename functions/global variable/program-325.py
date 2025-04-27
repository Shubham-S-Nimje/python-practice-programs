x=100 # Global Variable

def fun1():
    print(f'global variable x={x}')
def fun2():
    x=200 # Local variable
    print(f'local variable x={x}')

fun1()
fun2()
fun1()
