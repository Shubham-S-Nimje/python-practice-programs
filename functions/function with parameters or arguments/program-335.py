def fun1(a,b): # Required Parameters
    print(a,b)


def fun2(x,y,/): # Required positional only parameters
    print(x,y)
    

fun1(10,20) # Positional values or arguments
fun1(a=100,b=200) # Keyword arguments
fun1(b=99,a=88) # Keyword arguments
fun2(1,2) # Positional arguments
fun2(x=5,y=6) 
