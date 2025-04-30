x=100 #Global Variable
def fun1():
    y=200 #Local Varible
    def fun2():
        z=300 #Local Variable
        print(z)
        print(y)
        print(x)
        print(__name__)
         
    fun2()

fun1()
