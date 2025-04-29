def fun1(a,b,/): # function with required positional only
    print(f'a={a},b={b}')

def fun2(*,x,y): # function with required keyword only
    print(f'x={x},y={y}')

def fun3(a,b,/,*,x,y): #a,b are positional, x,y are keyword only
    print(f'a={a},b={b},x={x},y={y}')

fun1(100,200)
fun2(x=10,y=20)
#fun1(a=100,b=200) Error
#fun2(100,200) Error
fun3(1,2,x=3,y=4)
