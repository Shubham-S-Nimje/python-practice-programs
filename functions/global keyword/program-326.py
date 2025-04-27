a=100

def fun1():
    print(f'Global Variable a={a}')

def fun2():
    global a
    a=200
def fun3():
    global b
    b=300
# def fun4():
#     a=500 # local variable # Error
#     global a
#     a=600

fun1()
fun2()
fun1()
fun3()
print(f'Global variable b={b}')
# fun4()
