x=100 # Global Variable

def fun1():
    print(f'Global variable x={x}')
def fun2():
    x=200 # Local Variable
    print(f'Local variable x={x}')
    a=globals()
    print(f'Global variable x={a['x']}')
    x=400
    a['x']=900
    print(f'Local varible x={x}')
    print(f'Global variable x={a['x']}')

fun1()
fun2()
fun1()
