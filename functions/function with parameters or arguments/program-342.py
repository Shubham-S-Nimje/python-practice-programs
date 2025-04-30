def fun1(*a): # variable length positional parameter
    print(a,type(a))


fun1()
fun1(10)
fun1(10,20)
fun1(10,20,30,40,50)
fun1(10,"naresh",1.5,True,1+2j)
